import pandas as pd


def get_stats():
    return [
        {"label": "student accounts", "value": "107M"},
        {"label": "Hours of Code / Hours of AI served", "value": "1.94B"},
        {"label": "teachers supported", "value": "3M"},
        {"label": "countries", "value": "190"},
        {"label": "U.S. states with policy impact", "value": "50"}
    ]


def get_course_catalog():
    return [
        {
            "id": "course_a",
            "title": "Course A: First Steps",
            "level": "Beginner",
            "minutes": 45,
            "blocks": 20,
            "tags": ["Blocks", "Sequences", "Stories"],
            "description": "Build your very first programs with simple blocks and playful storytelling."
        },
        {
            "id": "course_b",
            "title": "Course B: Loops and Patterns",
            "level": "Beginner",
            "minutes": 60,
            "blocks": 28,
            "tags": ["Loops", "Art", "Patterns"],
            "description": "Make repeating patterns and colorful art while learning loops."
        },
        {
            "id": "course_c",
            "title": "Course C: Events and Games",
            "level": "Beginner",
            "minutes": 75,
            "blocks": 34,
            "tags": ["Events", "Games", "Sprites"],
            "description": "Create simple games with button presses and animations."
        },
        {
            "id": "course_d",
            "title": "Course D: Variables",
            "level": "Intermediate",
            "minutes": 90,
            "blocks": 42,
            "tags": ["Variables", "Math", "Games"],
            "description": "Learn variables and build score trackers for your games."
        },
        {
            "id": "course_e",
            "title": "Course E: Conditionals",
            "level": "Intermediate",
            "minutes": 95,
            "blocks": 45,
            "tags": ["Logic", "Conditionals", "Stories"],
            "description": "Add decision-making to stories and puzzles using if/else logic."
        },
        {
            "id": "course_f",
            "title": "Course F: Functions",
            "level": "Advanced",
            "minutes": 110,
            "blocks": 55,
            "tags": ["Functions", "Abstraction", "Art"],
            "description": "Create reusable blocks to build complex animations faster."
        }
    ]


def get_our_courses():
    return [
        {
            "title": "Curriculum for the AI era",
            "description": "Our newest high school course defines what meaningful AI education looks like in practice.",
            "cta": "Explore AI Foundations",
            "flagship": True,
            "icon": ""
        },
        {
            "title": "Coding Basics",
            "description": "Start your journey with fundamental programming concepts and logic building through interactive puzzles.",
            "cta": "Explore",
            "icon": "🎓"
        },
        {
            "title": "AI Foundations",
            "description": "Understand artificial intelligence, machine learning, and how AI is transforming industries.",
            "cta": "Explore",
            "icon": "🤖"
        },
        {
            "title": "Web Development",
            "description": "Build interactive websites using HTML, CSS, and JavaScript. Create projects that matter.",
            "cta": "Explore",
            "icon": "💻"
        },
        {
            "title": "Advanced Programming",
            "description": "Master advanced concepts and build production-ready applications with modern frameworks.",
            "cta": "Explore",
            "icon": "🚀"
        },
        {
            "title": "Data Science",
            "description": "Analyze data, create insights, and make data-driven decisions using Python and tools.",
            "cta": "Explore",
            "icon": "📊"
        },
        {
            "title": "Teacher Resources",
            "description": "Free professional development and curriculum materials for educators and trainers.",
            "cta": "Explore",
            "icon": "👨‍🏫"
        },
        {
            "title": "Setting the standard",
            "description": "We helped define the global AI Literacy Framework with governments and international institutions, shaping what students need to know in an AI-driven world.",
            "cta": "Read the AI Literacy Framework",
            "icon": "📚"
        },
        {
            "title": "System-level change",
            "description": "Lasting impact requires more than curriculum. We work with policymakers to make AI+CS education foundational, not optional.",
            "cta": "Join our movement to make AI and CS foundational, not optional",
            "icon": "🏛️"
        }
    ]


def get_pathways():
    return [
        {
            "name": "Creative Coding",
            "description": "Draw, animate, and design with code.",
            "steps": ["Patterns", "Pixel Art", "Animated Story"]
        },
        {
            "name": "Game Lab",
            "description": "Build games with sprites, scores, and levels.",
            "steps": ["Events", "Collisions", "Scoreboards"]
        },
        {
            "name": "Real-World Coding",
            "description": "Solve everyday challenges with logic.",
            "steps": ["Sorting", "Planning", "Mini Projects"]
        }
    ]


def get_projects():
    return [
        {
            "name": "Maze Runner",
            "type": "Game",
            "age_range": "Ages 8-10",
            "skills": ["Loops", "Events"]
        },
        {
            "name": "Dance Party",
            "type": "Animation",
            "age_range": "Ages 7-9",
            "skills": ["Timing", "Sequences"]
        },
        {
            "name": "Pet Simulator",
            "type": "Game",
            "age_range": "Ages 9-12",
            "skills": ["Variables", "Conditionals"]
        },
        {
            "name": "Story Spinner",
            "type": "Story",
            "age_range": "Ages 6-8",
            "skills": ["Choices", "Creativity"]
        },
        {
            "name": "Space Explorer",
            "type": "Adventure",
            "age_range": "Ages 10-12",
            "skills": ["Functions", "Scores"]
        },
        {
            "name": "Music Mixer",
            "type": "Music",
            "age_range": "Ages 8-11",
            "skills": ["Patterns", "Timing"]
        }
    ]


def get_testimonials():
    return [
        {
            "name": "Maya, Grade 4",
            "quote": "I built a game that my friends play at recess."
        },
        {
            "name": "Mr. Chen, Teacher",
            "quote": "The lessons are short, clear, and my class stays engaged."
        },
        {
            "name": "Aiden, Grade 6",
            "quote": "I learned how to make my own animations in one afternoon."
        }
    ]


def get_weekly_progress():
    data = {
        "week": ["Week 1", "Week 2", "Week 3", "Week 4", "Week 5", "Week 6"],
        "lessons_completed": [4, 6, 7, 5, 8, 9],
        "minutes": [35, 50, 58, 44, 66, 72]
    }
    return pd.DataFrame(data)


def get_skill_mix():
    data = {
        "skill": ["Sequences", "Loops", "Events", "Variables", "Conditionals"],
        "share": [28, 22, 20, 16, 14]
    }
    return pd.DataFrame(data)


def get_faq():
    return [
        {
            "question": "How long are the lessons?",
            "answer": "Most lessons are 20 to 45 minutes and designed to fit a class period."
        },
        {
            "question": "Do learners need experience?",
            "answer": "No experience needed. Each course starts with simple blocks."
        },
        {
            "question": "Can students share their projects?",
            "answer": "Yes, every project can be saved and shared with a link."
        }
    ]


def filter_courses(courses, level="All", tag="All", query=""):
    query_text = query.strip().lower()
    filtered = []
    for course in courses:
        if level != "All" and course["level"] != level:
            continue
        if tag != "All" and tag not in course["tags"]:
            continue
        if query_text:
            haystack = f"{course['title']} {course['description']} {' '.join(course['tags'])}".lower()
            if query_text not in haystack:
                continue
        filtered.append(course)
    return filtered


def build_blocks(prompt):
    text = prompt.strip().lower()
    if not text:
        return [
            "when run",
            "say 'Hello coder!'",
            "repeat 3 times",
            "move 10 steps"
        ]
    if "draw" in text or "art" in text or "paint" in text:
        return [
            "when run",
            "set pen color to 'teal'",
            "repeat 12 times",
            "move 20 steps",
            "turn 30 degrees"
        ]
    if "game" in text or "catch" in text or "score" in text:
        return [
            "when run",
            "create sprite 'player'",
            "on key press move 10 steps",
            "if touching 'star' then change score by 1"
        ]
    if "music" in text or "sound" in text:
        return [
            "when run",
            "repeat 4 times",
            "play sound 'beat'",
            "wait 0.5 seconds"
        ]
    return [
        "when run",
        "ask 'What should we build?'",
        "wait for answer",
        "say answer",
        "start next step"
    ]
