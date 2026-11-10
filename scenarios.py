"""
What your test runs. ← UNIT 8, MILESTONE 3

Each of your five criteria needs something run against it. A criterion about
false positives needs your own writing. One about label coverage needs inputs
across the score range. One about the appeal path needs a real content_id.

Working that out is Milestone 3's first step, and this file is where you write
it down. `run_eval.py` runs everything here three times.

Two are filled in as examples. Replace them with what your criteria actually
need — these are a shape, not a set.

A scenario carries **either** of these:

    "texts"   a list of strings. Each is sent as {"text": ..., "creator_id": ...}
              with a creator_id made up for you. Use this for most criteria.

    "bodies"  a list of whole request bodies, sent exactly as written. Use this
              when the malformed request IS the point — empty text, no `text`
              field at all, something enormous. A bad-input criterion needs it,
              because you cannot express "the field is missing" as a string.
"""

# ⚠️ My own writing. Not AI text, not a sample from the web — things I actually
# wrote. Criterion 1 uses all ten; criteria 2 and 4 reuse five of them.
MY_WRITING = [
            "With the specific two pieces of Jordan’s arts mentioned above, both portray how technologies and how the human behaving of mass consumers has negatively affected the environment. As “Art Works for Change” informs, “the U.S. generates more total e-waste per year – 9.4 million tons – than any other country.” As a new version of hone is coming out frequently, consumers will throw away their old iPhone or old electronics to buy a new one. These old products will end up in waste and stack up in landfills. Not only so, “the toxic metals and flame retardants they contain can cause environmental problems.” These toxic chemicals can eventually transfer to the air that we breathe in, and these toxic trails will still go on to not only put harm on humans but also destroy the environment. These arts criticize the image of mass consumption to the ignorance of human waste that causes damage to the environment.",
            "A meaningful piece of work that everybody can find their own meaning and joy in is called art. Art is a work of life that contains one’s feelings and emotions. This is all my definition of art. I cannot find myself describing art in a single line of definition because, as I said, art is work that contains life, and to make a short and simple definition of it would be impossible for me. ",
            "Having the option to live in America as a Vietnamese is quite precious. It has changed my life, and I have had many wonderful experiences here that I would not have had if I lived in Vietnam.",
            "As my mom’s car stopped at the red light crossing the plaza, I already saw the mall. The building designs mixing of Vietnamese and Chinese styles. The outside of the building is in the shape of one big square in the middle of the two small squares. ",
            "In the front of the supermarket, it was a line of 8 cashiers. It was kind of crowded and busy as it was Sunday when I went there. Each line of the cashiers had at least three or four people waiting. People tried to pack stuff on their carts after checking out. One woman’s cart was full of plastic bags which I can see some green vegetables poking out of it.",
            "In the end, our cart was as full as the first lady that I saw when coming to the supermarket, except we did not have the two packs of rice. After spending time here, I mostly felt grateful that there was a place like this in America. This Vietnamese supermarket brings people within the same background and ethnicity together. Even though we live in a country where English is the official language, and where western culture dominates, it does not mean that we have to forget our background and our culture.",
            "This order of writing does not only help me to write more smoothly, but it also creates a line of story or plot for both organized and comprehensible purposes. With this organization, after each observation or context, I will explain or analyze those observations in more detail and how it relates to the main theme or connects it to the larger context within the community.",
            "On a summer day in Denton, Texas, I was about to hang out and have dinner with my sister and my cousin who studied in New Mexico but decided to come to stay with us in Texas throughout the summer. The appearance of my cousin had made this ordinary day a little bit special than usual. It was his last week staying with us before flying back to New Mexico, so we were really excited to be by ourselves and enjoy our time together before he leaves.",
            "My name is Linh Tran. I am living in Texas and a student at the University of North Texas. I just turned 18 this year, which starts the age of my voting right. I have been listened to and noticed more political issues and contents than ever in my life. One of the standpoints that I would not agree with before but now is the idea of how everything in life is political. I am a constituent. One of the political issues that I am concerned about is the climate crisis. The reason why I feel so pressured about this issue is that as a young adult, I feel my future is threatened by the dangers of climate change.",
            "The reason why I writing this letter to you is that I saw your bill, H.Res.332, of the Green New Deal. The resolution is a good start to reducing climate change by focusing on a better living condition of Americans with the providing of good energy and powers that will reduce the greenhouse gas. Specifically, transportation takes a lot of percent in creating carbon footprint and causing pollution. Therefore, there should be a more powerful act in reducing the fossil fuel emissions of gas in transportation and increasing or putting electric cars into use."
]

# Five chatbot-generated texts, on the same topics as my five human pieces
# below, so the only difference between the two groups is who wrote them.
AI_TEXTS = [
    "Art has long served as a powerful lens through which we can examine the relationship between humanity and the natural world. In recent years, many contemporary artists have turned their attention to the growing problem of electronic waste. By transforming discarded phones, circuit boards, and cables into striking visual works, these artists invite viewers to confront the hidden consequences of consumer culture. Each year, millions of tons of electronic devices are thrown away, and many end up in landfills where toxic materials can seep into the soil and water. Through their work, artists remind us that every purchase has an environmental cost. Ultimately, art can inspire meaningful reflection and encourage more sustainable choices.",
    "Visiting a Vietnamese supermarket in America can be a deeply meaningful experience. The aisles are filled with familiar ingredients, from fresh herbs and rice noodles to fish sauce and tropical fruits, creating a sense of connection to home. Beyond simply providing groceries, these stores serve as important community spaces where people of similar backgrounds can come together. Shoppers often exchange greetings in their native language, share recipes, and celebrate cultural traditions. For many immigrant families, these markets help preserve their heritage while they adapt to life in a new country. In this way, a simple trip to the supermarket becomes a powerful reminder that cultural identity can thrive even far from home.",
    "Summer days have a unique way of bringing people closer together. Spending time with family members, especially those who live far away, can turn an ordinary afternoon into a cherished memory. Whether it is sharing a meal at a favorite restaurant, exploring a new part of town, or simply talking late into the evening, these moments help strengthen the bonds between loved ones. When a visit is coming to an end, there is often a sense of urgency to make the most of the remaining time. These experiences remind us that the people we care about are what truly make life meaningful, and that time spent together is always worth treasuring.",
    "Climate change is one of the most pressing challenges facing young people today. As rising temperatures, extreme weather events, and sea level rise become more common, many young adults feel a growing sense of urgency about the future. Becoming eligible to vote is an important milestone, as it provides an opportunity to influence the policies that will shape the world for decades to come. By staying informed, engaging with elected officials, and supporting candidates who prioritize environmental protection, young voters can make their voices heard. Ultimately, addressing the climate crisis will require collective action, and every individual has a role to play in creating a more sustainable future.",
    "I am writing to express my strong support for the Green New Deal resolution and to encourage you to continue advocating for meaningful climate action. The resolution represents an important step toward reducing greenhouse gas emissions while also creating good jobs and improving living conditions for Americans. In particular, I believe the transportation sector deserves special attention, as it is one of the largest contributors to carbon emissions in the United States. Expanding access to electric vehicles, investing in public transportation, and modernizing infrastructure would significantly reduce pollution. Thank you for your leadership on this critical issue. I hope you will continue to prioritize policies that protect our environment for future generations.",
]

SCENARIOS = [
    {
        "name": "my own writing",
        "criterion": 1,
        "texts": MY_WRITING,
    },
    {
        # Criteria 2 AND 4 use this same set: 5 human texts, then 5 AI texts.
        #   Criterion 2: average confidence of items 6-10 minus items 1-5 >= 0.5
        #   Criterion 4: at most 1 "unsure" in items 1-5 and at most 1 in 6-10
        "name": "human vs AI",
        "criterion": "2 and 4",
        "texts": [MY_WRITING[i] for i in (0, 5, 7, 8, 9)] + AI_TEXTS,
    },
    {
        # Criterion 3: under 15 words (or no text at all) gets a response telling
        # the writer the text is missing or too short. Bodies 1-6 should all be
        # refused that way. Body 7 is a CONTROL — exactly 15 words — and should
        # be accepted and scored, so the check isn't just "refuse everything".
        "name": "missing or short text",
        "criterion": 3,
        "bodies": [
            {"creator_id": "eval_bad_missing"},                    # no text field
            {"text": "", "creator_id": "eval_bad_empty"},
            {"text": "   \n\t  ", "creator_id": "eval_bad_whitespace"},
            {"text": None, "creator_id": "eval_bad_null"},
            {"text": "Hello.", "creator_id": "eval_bad_one_word"},
            {"text": "I wrote this short note to test whether the service "
                     "rejects text this short.",                     # 14 words
             "creator_id": "eval_bad_14_words"},
            {"text": "I wrote this short note to test whether the service "
                     "rejects text this short today.",               # 15 words
             "creator_id": "eval_ok_15_words"},
        ],
    },
    {
        # Criterion 5: every valid appeal is logged with its content_id,
        # event "appeal" and status "under_review". run_eval.py submits each
        # text, appeals the content_id that comes back, then reads /log to
        # check the entry. It also sends one appeal for a content_id that
        # doesn't exist, which should be refused and NOT logged.
        "name": "appeal path",
        "criterion": 5,
        "appeals": [MY_WRITING[1], MY_WRITING[4], MY_WRITING[6]],
    },
    # A bad-input criterion looks like this. Uncomment and adjust if that's one
    # of your five — these are raw request bodies, sent exactly as written.
    #
    # {
    #     "name": "bad input",
    #     "criterion": 3,
    #     "bodies": [
    #         {"text": "", "creator_id": "eval_bad_empty"},
    #         {"creator_id": "eval_bad_missing"},          # no text field at all
    #         {"text": "word " * 50000, "creator_id": "eval_bad_huge"},
    #         {"text": None, "creator_id": "eval_bad_null"},
    #     ],
    # },

    # TODO: add what your remaining criteria need.
    #
    # A criterion about the appeal path can't be tested by sending text alone;
    # it needs a submission first and then an appeal against the content_id
    # that came back. You'll need to test that one by hand, or extend this file
    # and run_eval.py to do it. Saying which you did is part of the write-up.
]


def validate() -> list[str]:
    """
    Complain about anything malformed, before a long run rather than during.

    A "bodies" scenario is deliberately exempt from the empty check — an empty
    string is the whole point of a bad-input case, and refusing to run one
    would make that criterion untestable.
    """
    problems = []
    for i, scenario in enumerate(SCENARIOS, 1):
        if not scenario.get("name"):
            problems.append(f"scenario {i} has no name")

        texts = scenario.get("texts")
        bodies = scenario.get("bodies")

        if "appeals" in scenario:
            if texts or bodies:
                problems.append(
                    f"scenario {i} ('{scenario.get('name')}') has appeals plus "
                    f"texts or bodies — pick one"
                )
            elif not scenario["appeals"]:
                problems.append(f"scenario {i} has an empty appeals list")
            continue

        if texts and bodies:
            problems.append(
                f"scenario {i} ('{scenario.get('name')}') has both texts and "
                f"bodies — pick one"
            )
            continue

        if bodies:
            for j, body in enumerate(bodies, 1):
                if not isinstance(body, dict):
                    problems.append(
                        f"scenario {i}, body {j} is not a dict — bodies are whole "
                        f"request bodies, like {{'text': '', 'creator_id': 'x'}}"
                    )
            continue

        if not texts:
            problems.append(f"scenario {i} has no texts and no bodies")
            continue

        for j, text in enumerate(texts, 1):
            if not str(text).strip():
                problems.append(
                    f"scenario {i}, text {j} is empty — if an empty submission is what "
                    f"you're testing, use 'bodies' instead of 'texts'"
                )
            elif str(text).startswith("REPLACE ME"):
                problems.append(
                    f"scenario {i} ('{scenario.get('name')}'), text {j} is still "
                    f"the placeholder"
                )
    return problems
