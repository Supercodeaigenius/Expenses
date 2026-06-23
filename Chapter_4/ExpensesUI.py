# ExpensesUI.py
# Streamlit UI that mimics an Excel expenses form: fixed header row, boxed cells,
# and editable rows underneath.

from __future__ import annotations

from datetime import date
from pathlib import Path

import pandas as pd
import streamlit as st


TABLE_COLUMNS = [
    "Date",
    "Gross £",
    "VAT £",
    "Net £",
    "VAT rate",
    "N/L code (office use)",
    "Client name(s) #",
    "Nature of expense*",
    "Description",
    "Receipt No.",
]


def _default_df(rows: int = 15) -> pd.DataFrame:
    df = pd.DataFrame({col: [""] * rows for col in TABLE_COLUMNS})
    # Ensure the editor sees a true date-like dtype (not string).
    df["Date"] = pd.NaT
    df["Receipt No."] = list(range(1, rows + 1))
    return df


def _ensure_columns(df: pd.DataFrame) -> pd.DataFrame:
    df = df.copy()
    df.columns = [str(c).strip() for c in df.columns]
    for col in TABLE_COLUMNS:
        if col not in df.columns:
            df[col] = pd.NaT if col == "Date" else ""
    return df[TABLE_COLUMNS]


def _coerce_number(series: pd.Series) -> pd.Series:
    # Accept blanks/strings and turn them into NaN for safe arithmetic.
    return pd.to_numeric(series, errors="coerce")


def _recompute(df: pd.DataFrame) -> pd.DataFrame:
    df = _ensure_columns(df)

    gross = _coerce_number(df["Gross £"])
    vat = _coerce_number(df["VAT £"])

    # Net is derived; show blank unless both inputs are present.
    net = gross - vat
    df["Net £"] = net.where(gross.notna() & vat.notna(), "")

    # VAT rate: mimic Excel's #DIV/0! when Net is missing/zero.
    net_num = _coerce_number(df["Net £"])
    rate = vat / net_num
    df["VAT rate"] = rate.map(lambda x: "" if pd.isna(x) else f"{x:.2%}")
    df.loc[net_num.isna() | (net_num == 0), "VAT rate"] = "#DIV/0!"

    # Keep receipt numbers sequential.
    df["Receipt No."] = list(range(1, len(df) + 1))
    return df


def _load_default_df() -> pd.DataFrame:
    return _recompute(_default_df())


def _load_css(path: Path) -> str:
    if path.exists():
        return path.read_text(encoding="utf-8")
    return ""


def render_expenses_ui() -> None:
    st.title("Expenses Application")

    st.session_state.setdefault("claimant_name", "")
    st.session_state.setdefault("claimant_date", date.today())
    st.session_state.setdefault("expense_type", "")
    st.session_state.setdefault("claimant_signature", "")
    st.session_state.setdefault("approved_by", "")
    st.session_state.setdefault("approval_position", "")
    st.session_state.setdefault("approval_signature", "")
    st.session_state.setdefault("approval_date", date.today())
    st.session_state.setdefault("menu_message", "")
    st.session_state.setdefault("show_expense_page", False)
    st.session_state.setdefault("show_approval_page", False)
    st.session_state.setdefault("show_guidance", False)
    st.session_state.setdefault("approved_expense", False)

    st.sidebar.title("Expense Menu")
    if st.sidebar.button("➕ Create Expense"):
        st.session_state.expenses_df = _load_default_df()
        st.session_state.menu_message = "Created a new expense form."
        st.session_state.approved_expense = False
        st.session_state.show_guidance = False
        st.session_state.show_expense_page = True
    if st.sidebar.button("💾 Save Changes"):
        st.session_state.menu_message = "Changes saved successfully."
        st.session_state.show_guidance = False
        st.session_state.show_expense_page = True
    if st.sidebar.button("✅ Approved Expense"):
        st.session_state.menu_message = "Expense moved to Approved Expense section."
        st.session_state.approved_expense = True
        st.session_state.show_approval_page = True
        st.session_state.show_guidance = False
        st.session_state.show_expense_page = False
    if st.sidebar.button("👁️ View Expense"):
        st.session_state.menu_message = "Viewing current expense form."
        st.session_state.show_expense_page = True
        st.session_state.show_guidance = False
    if st.sidebar.button("📄 T&C"):
        st.session_state.menu_message = "Showing terms and guidance page."
        st.session_state.show_guidance = True
        st.session_state.show_expense_page = False

    if st.session_state.get("menu_message"):
        st.info(st.session_state.menu_message)

    if st.session_state.show_guidance:
        st.title("Expense Guidance & Terms")
        if st.button("← Back to Main Page"):
            st.session_state.show_guidance = False
        st.markdown(
            """
            ### Expense guidance
            - **Client name(s)** - NB please ensure client(s) details and/or event details are completed in each case.
            - **Nature of expense** - Please specify the type of expense.
            - **Travel**: Rail travel, taxi fares, air fare, car mileage, parking costs.
            - **Subsistence**: Hotel bill, meal costs whilst working away, books/publications.
            - **Internet costs**: E.g. dial-up costs whilst working away, home broadband where permitted.
            - **Entertainment**: Client Entertaining, Staff Entertaining, Golf trip etc - please specify whether client, staff and client or staff-only and include details of attendees and the occasion in Description.
            - **Phone costs**: Please specify home, mobile etc.
            - **Office costs**: Printing, stationery, postage, refreshments (coffee, milk etc for office).
            - **Subscriptions**: Please specify the nature of the expense.
            - **Software costs**: Please specify the nature of the expense.

            ### Terms & Conditions
            - All expenses must be supported by valid receipts.
            - Ensure expense descriptions are clear and complete.
            - All submissions must follow the company expense policy.
            - Approval is required before processing reimbursable expenses.
            """
        )
        return

    if st.session_state.show_approval_page:
        st.title("Approval Details")
        if st.button("← Back to Main Page"):
            st.session_state.show_approval_page = False
        st.markdown("---")

        st.subheader("Approval details")
        approval_col1, approval_col2, approval_col3 = st.columns([2, 2, 1])
        with approval_col1:
            st.text_input("Approved by", key="approved_by")
            st.text_input("Position", key="approval_position")
        with approval_col2:
            st.text_input("Approval signature", key="approval_signature")
        with approval_col3:
            st.date_input("Approval date", key="approval_date")

        st.markdown("---")
        return

    if st.session_state.show_expense_page:
        st.title("Expense Form")
        if st.button("← Back to Main Page"):
            st.session_state.show_expense_page = False
        st.markdown("---")

        # Header and grid styling to match the screenshot (boxed cells, thick header rule,
        # and grey "office use" columns.
        css_path = Path(__file__).with_suffix(".css")
        css = _load_css(css_path)
        if css:
            st.markdown(css, unsafe_allow_html=True)

        if "expenses_df" not in st.session_state:
            st.session_state.expenses_df = _load_default_df()

        st.caption("Rows are editable. Use the + control to add more rows.")

        df = st.session_state.expenses_df.copy()
        # Keep as datetime64[ns] so Streamlit's DateColumn is compatible for editing.
        df["Date"] = pd.to_datetime(df["Date"], errors="coerce")

        edited_df = st.data_editor(
            df,
            num_rows="dynamic",
            width="stretch",
            hide_index=True,
            disabled=["Net £", "VAT rate", "Receipt No."],
            column_config={
                "Date": st.column_config.DateColumn("Date", format="DD/MM/YYYY", width="small"),
                "Gross £": st.column_config.NumberColumn("Gross £", format="£ %.2f", width="small"),
                "VAT £": st.column_config.NumberColumn("VAT £", format="£ %.2f", width="small"),
                "Net £": st.column_config.NumberColumn("Net £", format="£ %.2f", width="small"),
                "VAT rate": st.column_config.TextColumn("VAT rate", width="small"),
                "N/L code (office use)": st.column_config.TextColumn("N/L code\n(office use)", width="small"),
                "Client name(s) #": st.column_config.TextColumn("Client name(s) #", width="medium"),
                "Nature of expense*": st.column_config.TextColumn("Nature of expense*", width="medium"),
                "Description": st.column_config.TextColumn("Description", width="large"),
                "Receipt No.": st.column_config.NumberColumn("Receipt No.", width="small"),
            },
            key="expenses_editor",
        )

        st.session_state.expenses_df = _recompute(edited_df)

        total_gross = _coerce_number(st.session_state.expenses_df["Gross £"]).sum(skipna=True)
        total_vat = _coerce_number(st.session_state.expenses_df["VAT £"]).sum(skipna=True)
        total_net = _coerce_number(st.session_state.expenses_df["Net £"]).sum(skipna=True)

        total_col1, total_col2, total_col3 = st.columns(3)
        total_col1.metric("Total Gross £", f"£{total_gross:,.2f}")
        total_col2.metric("Total VAT £", f"£{total_vat:,.2f}")
        total_col3.metric("Total Net £", f"£{total_net:,.2f}")

        return

    st.subheader("Claimant information")
    top_col1, top_col2, top_col3, top_col4 = st.columns([2, 1, 2, 2])
    with top_col1:
        st.text_input("Name", key="claimant_name")
    with top_col2:
        st.date_input("Date", key="claimant_date")
    with top_col3:
        st.text_input("Type of expense", key="expense_type", placeholder="Amex / Expenses etc")
    with top_col4:
        st.text_input("Claimant signature", key="claimant_signature")

    st.markdown("---")

    if st.session_state.show_expense_page:
        st.title("Expense Form")
        if st.button("← Back to Main Page"):
            st.session_state.show_expense_page = False
        st.markdown("---")

        # Header and grid styling to match the screenshot (boxed cells, thick header rule,
        # and grey "office use" columns.
        css_path = Path(__file__).with_suffix(".css")
        css = _load_css(css_path)
        if css:
            st.markdown(css, unsafe_allow_html=True)

        if "expenses_df" not in st.session_state:
            st.session_state.expenses_df = _load_default_df()

        st.caption("Rows are editable. Use the + control to add more rows.")

        df = st.session_state.expenses_df.copy()
        # Keep as datetime64[ns] so Streamlit's DateColumn is compatible for editing.
        df["Date"] = pd.to_datetime(df["Date"], errors="coerce")

        edited_df = st.data_editor(
            df,
            num_rows="dynamic",
            width="stretch",
            hide_index=True,
            disabled=["Net £", "VAT rate", "Receipt No."],
            column_config={
                "Date": st.column_config.DateColumn("Date", format="DD/MM/YYYY", width="small"),
                "Gross £": st.column_config.NumberColumn("Gross £", format="£ %.2f", width="small"),
                "VAT £": st.column_config.NumberColumn("VAT £", format="£ %.2f", width="small"),
                "Net £": st.column_config.NumberColumn("Net £", format="£ %.2f", width="small"),
                "VAT rate": st.column_config.TextColumn("VAT rate", width="small"),
                "N/L code (office use)": st.column_config.TextColumn("N/L code\n(office use)", width="small"),
                "Client name(s) #": st.column_config.TextColumn("Client name(s) #", width="medium"),
                "Nature of expense*": st.column_config.TextColumn("Nature of expense*", width="medium"),
                "Description": st.column_config.TextColumn("Description", width="large"),
                "Receipt No.": st.column_config.NumberColumn("Receipt No.", width="small"),
            },
            key="expenses_editor",
        )

        st.session_state.expenses_df = _recompute(edited_df)

        total_gross = _coerce_number(st.session_state.expenses_df["Gross £"]).sum(skipna=True)
        total_vat = _coerce_number(st.session_state.expenses_df["VAT £"]).sum(skipna=True)
        total_net = _coerce_number(st.session_state.expenses_df["Net £"]).sum(skipna=True)

        total_col1, total_col2, total_col3 = st.columns(3)
        total_col1.metric("Total Gross £", f"£{total_gross:,.2f}")
        total_col2.metric("Total VAT £", f"£{total_vat:,.2f}")
        total_col3.metric("Total Net £", f"£{total_net:,.2f}")

        return

    st.markdown("---")


if __name__ == "__main__":
    render_expenses_ui()
