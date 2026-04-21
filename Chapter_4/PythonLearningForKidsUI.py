import streamlit as st
import altair as alt
from pathlib import Path

from PythonLearningForKids import (
    get_stats,
    get_course_catalog,
    get_pathways,
    get_projects,
    get_testimonials,
    get_weekly_progress,
    get_skill_mix,
    get_faq,
    filter_courses,
    build_blocks
)
from PythonLearningForKidsUIMathsQuiz import render_math_quiz_page


st.set_page_config(page_title="Python Learning for Kids", layout="wide")

css_path = Path(__file__).with_name("PythonLearningForKidsUICSS.css")
st.markdown(f"<style>{css_path.read_text(encoding='utf-8')}</style>", unsafe_allow_html=True)

selected_page = st.query_params.get("page", "")
if isinstance(selected_page, list):
    selected_page = selected_page[0] if selected_page else ""
if selected_page == "PythonLearningForKidsUIMathsQuiz":
    render_math_quiz_page()
    st.stop()


def render_pills(tags):
    return "".join([f"<span class='pill'>{tag}</span>" for tag in tags])


def render_course_card(course):
    return f"""
    <div class='card'>
        <h4>{course['title']}</h4>
        <p>{course['description']}</p>
        <div>{render_pills(course['tags'])}</div>
        <p><strong>Level:</strong> {course['level']} | <strong>Blocks:</strong> {course['blocks']} | <strong>Minutes:</strong> {course['minutes']}</p>
    </div>
    """


def render_project_card(project):
    return f"""
    <div class='card'>
        <h4>{project['name']}</h4>
        <p><strong>Type:</strong> {project['type']}</p>
        <p><strong>Age:</strong> {project['age_range']}</p>
        <div>{render_pills(project['skills'])}</div>
    </div>
    """


stats = get_stats()
courses = get_course_catalog()
pathways = get_pathways()
projects = get_projects()
testimonials = get_testimonials()
weekly = get_weekly_progress()
skill_mix = get_skill_mix()
faq = get_faq()

st.markdown(
    """
    <div class='notice'>
        <span>Hour of AI activities are now live.</span>
        <a>Get started</a>
    </div>
    <div class='codeorg-nav'>
        <div class='codeorg-nav-logo'>PYTHON KIDS</div>
        <div class='codeorg-nav-links'>
            <span>Learn</span>
            <a href='?page=PythonLearningForKidsUIMathsQuiz' target='_self'>Teach</a>
            <span>Districts</span>
            <span>Stats</span>
            <span>Donate</span>
            <span>Incubator</span>
            <span>About</span>
        </div>
        <div class='codeorg-nav-cta'>
            <span class='nav-signin'>Sign in</span>
            <span class='nav-donate'>Donate</span>
        </div>
    </div>
    """,
    unsafe_allow_html=True
)

hero_cols = st.columns([2.1, 1])
with hero_cols[0]:
    st.markdown(
        """
        <div class='hero'>
            <div class='hero-title'>AI is reshaping the world</div>
            <div class='hero-kicker'>Education must lead what comes next</div>
            <div class='hero-sub'>The Hour of Code sparked a generation. This fall, the Hour of AI will define the next.</div>
        """,
        unsafe_allow_html=True
    )
    cta_cols = st.columns([1, 1])
    with cta_cols[0]:
        st.button("Get started!", type="primary")
    with cta_cols[1]:
        st.button("Explore curriculum")
    st.markdown("</div>", unsafe_allow_html=True)

with hero_cols[1]:
    st.markdown(
        """
        <div class='hero-card'>
            <h4>It's here: the newest Hour of AI activity</h4>
            <p>Bring AI, creativity, and students together with Mix &amp; Move with AI.</p>
            <div class='pill'>Loops</div>
            <div class='pill'>Events</div>
            <div class='pill'>Stories</div>
            <p><strong>Suggested age:</strong> 7-11</p>
        </div>
        """,
        unsafe_allow_html=True
    )

stat_cols = st.columns(len(stats))
for col, item in zip(stat_cols, stats):
    with col:
        st.markdown(
            f"""
            <div class='stat'>
                <div class='stat-label'>{item['label']}</div>
                <div class='stat-value'>{item['value']}</div>
            </div>
            """,
            unsafe_allow_html=True
        )

st.markdown(
    """
    <div class='section'>
        <div class='section-eyebrow'>Who we are</div>
        <div class='section-title'>We are the experts in preparing students for an AI-driven world.</div>
        <div class='section-sub'>AI is built on CS. We teach both.</div>
    </div>
    """,
    unsafe_allow_html=True
)

pathway_cols = st.columns(3)
for col, path in zip(pathway_cols, pathways):
    with col:
        st.markdown(
            f"""
            <div class='card'>
                <h4>{path['name']}</h4>
                <p>{path['description']}</p>
                <p><strong>Steps:</strong> {", ".join(path['steps'])}</p>
            </div>
            """,
            unsafe_allow_html=True
        )

st.markdown("<div class='section-title'>Course Catalog</div>", unsafe_allow_html=True)
st.markdown("<div class='section-sub'>Filter by level or skills to match a perfect lesson.</div>", unsafe_allow_html=True)

filter_cols = st.columns([1, 1, 2])
with filter_cols[0]:
    level_filter = st.selectbox("Level", ["All", "Beginner", "Intermediate", "Advanced"])
with filter_cols[1]:
    all_tags = sorted({tag for course in courses for tag in course["tags"]})
    tag_filter = st.selectbox("Skill Tag", ["All"] + all_tags)
with filter_cols[2]:
    query = st.text_input("Search", placeholder="Try 'games', 'loops', or 'stories'")

filtered_courses = filter_courses(courses, level_filter, tag_filter, query)

if not filtered_courses:
    st.info("No courses match those filters yet. Try a different level or tag.")
else:
    card_cols = st.columns(3)
    for idx, course in enumerate(filtered_courses):
        with card_cols[idx % 3]:
            st.markdown(render_course_card(course), unsafe_allow_html=True)

st.markdown("<div class='section-title'>Block Builder</div>", unsafe_allow_html=True)
st.markdown("<div class='section-sub'>Describe what you want to make and see the building blocks.</div>", unsafe_allow_html=True)
prompt = st.text_input("What do you want to build?", placeholder="A catching game with a score")
blocks = build_blocks(prompt)
st.code("\n".join(blocks))

st.markdown(
    """
    <div class='section'>
        <div class='section-title'>Project Gallery</div>
        <div class='section-sub'>Remix starter projects or share your own.</div>
    </div>
    """,
    unsafe_allow_html=True
)

project_cols = st.columns(3)
for idx, project in enumerate(projects):
    with project_cols[idx % 3]:
        st.markdown(render_project_card(project), unsafe_allow_html=True)

st.markdown(
    """
    <div class='section'>
        <div class='section-title'>Share Your Project</div>
        <div class='section-sub'>Save your work and get feedback from friends.</div>
    </div>
    """,
    unsafe_allow_html=True
)
share_cols = st.columns([2, 1])
with share_cols[0]:
    project_name = st.text_input("Project name", placeholder="My Super Game")
    project_desc = st.text_area("Describe your project", placeholder="What makes it special?")
with share_cols[1]:
    st.selectbox("Project type", ["Game", "Story", "Animation", "Music"])
    st.selectbox("Skill focus", ["Loops", "Events", "Variables", "Conditionals"])
    st.button("Save Project")

if project_name and project_desc:
    st.success("Nice work. Your project is ready to share.")

st.markdown("<div class='section-title'>Learning Progress</div>", unsafe_allow_html=True)
st.markdown("<div class='section-sub'>Track weekly growth and skill balance.</div>", unsafe_allow_html=True)

chart_cols = st.columns(2)
with chart_cols[0]:
    line_chart = (
        alt.Chart(weekly)
        .mark_line(point=True, color="#00a3ad")
        .encode(
            x=alt.X("week", title="Week"),
            y=alt.Y("lessons_completed", title="Lessons Completed")
        )
    )
    st.altair_chart(line_chart, use_container_width=True)

with chart_cols[1]:
    bar_chart = (
        alt.Chart(skill_mix)
        .mark_bar(color="#f7b500")
        .encode(
            x=alt.X("share", title="Share"),
            y=alt.Y("skill", sort="-x", title="Skill")
        )
    )
    st.altair_chart(bar_chart, use_container_width=True)

st.markdown(
    """
    <div class='section'>
        <div class='band'>
            <h3>Join the movement</h3>
            <p>As a nonprofit, we provide this work to schools for free. Partners help scale AI education for every student.</p>
            <p><strong>New:</strong> Hour of AI activities and professional learning.</p>
        </div>
    </div>
    """,
    unsafe_allow_html=True
)

st.markdown("<div class='section-title'>Student Stories</div>", unsafe_allow_html=True)
story_cols = st.columns(3)
for col, story in zip(story_cols, testimonials):
    with col:
        st.markdown(
            f"""
            <div class='card'>
                <p>"{story['quote']}"</p>
                <p><strong>{story['name']}</strong></p>
            </div>
            """,
            unsafe_allow_html=True
        )

st.markdown("<div class='section-title'>Educator Corner</div>", unsafe_allow_html=True)
st.markdown("<div class='section-sub'>Tools for classrooms, clubs, and at-home learning.</div>", unsafe_allow_html=True)

educator_cols = st.columns([1, 2])
with educator_cols[0]:
    st.markdown(
        """
        <div class='card'>
            <h4>Class Setup</h4>
            <p>Create a section, invite students, and track progress.</p>
            <p><strong>Average setup time:</strong> 10 minutes</p>
        </div>
        """,
        unsafe_allow_html=True
    )
    st.markdown(
        """
        <div class='card'>
            <h4>Printable Guides</h4>
            <p>Download offline activities and posters for the classroom.</p>
        </div>
        """,
        unsafe_allow_html=True
    )
with educator_cols[1]:
    st.markdown("<div class='section-title'>Frequently Asked Questions</div>", unsafe_allow_html=True)
    for item in faq:
        with st.expander(item["question"]):
            st.write(item["answer"])

st.markdown("<div class='footer'>Built for curious kids, supported by educators, powered by Python.</div>", unsafe_allow_html=True)
