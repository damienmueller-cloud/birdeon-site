#!/usr/bin/env python3
"""Generate the Birdeon static preview site."""
from __future__ import annotations

import json
import os
from html import escape
from pathlib import Path

ROOT = Path("/workspace/fore-golf/birdeon-site")
SITE = "https://birdeon.com"
SIZES = json.loads(Path("/tmp/img-sizes.json").read_text())

CATALOGUES = {
    "highland-hole-out": {
        "name": "Highland Hole Out",
        "tagline": "Neon and navy tartan for the course.",
        "eyebrow": "Collection one",
        "title": "Highland Hole Out | Tartan Golf Apparel | Birdeon",
        "description": "Explore Birdeon's Highland Hole Out collection: men's tartan golf polos and shorts, women's golf polos with reverse-colour tartan skirts, leather-patch golf caps and a navy tartan golf bag. Coming soon in Australia, the Philippines and Taiwan.",
        "intro": "Highland Hole Out is Birdeon's tartan collection — navy grounds crossed with purple and orange, a black tartan with neon pink and lime, and brighter women's colourways where the skirt is cut in the reverse of the polo. Each look is shown as a polo, bottom, cap and socks. Products will be available soon.",
        "hero": "edd-course-black-neon-leather",
        "tile": "herrera-reverse-pink-lemon",
        "tile_alt": "Woman wearing a pink and lemon tartan golf polo and reverse-colour pleated golf skirt from Birdeon's Highland Hole Out collection",
    },
    "winter-league": {
        "name": "Winter League",
        "tagline": "Darker layers for cooler rounds.",
        "eyebrow": "Collection two",
        "title": "Winter League | Winter Golf Trousers and Layers | Birdeon",
        "description": "Birdeon Winter League golf apparel: men's charcoal golf trousers, a forest quarter-zip and a darker navy tartan polo, plus a women's burgundy tartan polo and forest tartan golf skirt. Coming soon.",
        "intro": "Winter League takes the palette darker for cooler days on the course. The men's set is built around charcoal full-length golf trousers and a forest green quarter-zip worn over a navy tartan polo. The women's set keeps a pleated tartan golf skirt, paired with a burgundy tartan polo and burgundy details. Fabric details coming soon. Products will be available soon.",
        "hero": "winter-edd-course",
        "tile": "winter-herrera",
        "tile_alt": "Woman wearing a burgundy tartan golf polo and forest tartan skirt from Birdeon's Winter League collection",
    },
    "summer-links": {
        "name": "Summer Links",
        "tagline": "Bright, plain colour for warm weather.",
        "eyebrow": "Collection three",
        "title": "Summer Links | Coral and Aqua Golf Apparel | Birdeon",
        "description": "Birdeon Summer Links: bright, plain coral and aqua golf apparel — a men's coral golf polo with aqua shorts, and a women's aqua polo with a coral pleated golf skirt. Coming soon for warm-weather golf in Australia, the Philippines and Taiwan.",
        "intro": "Summer Links is the plain-colour counterpart to Birdeon's tartan collections. Coral and aqua are used in clean blocks — a coral men's golf polo with aqua shorts, and a women's aqua polo with a coral pleated skirt — cut for warm rounds and travel days. Fabric details coming soon. Products will be available soon.",
        "hero": "summer-edd-course",
        "tile": "summer-herrera",
        "tile_alt": "Woman wearing an aqua golf polo and coral pleated golf skirt from Birdeon's Summer Links collection",
    },
}

# Product records. images: list of (stem, alt). First image is the card/hero.
PRODUCTS: list[dict] = []


def P(**kwargs):
    PRODUCTS.append(kwargs)
    return kwargs


# ---------- Highland men ----------
P(
    slug="mens-navy-tartan-golf-polo",
    name="Men's Navy Tartan Golf Polo",
    short="Navy, purple and orange tartan with an orange collar.",
    catalogue="highland-hole-out",
    group="highland-navy-men",
    kind="Men's golf polo",
    images=[
        ("edd-beach-navy-leather", "Man kneeling on a tropical beach wearing the Birdeon men's navy tartan golf polo, navy shorts and navy cap"),
        ("edd-forepack-purple-v2", "Man standing on a golf course in the Birdeon men's navy tartan golf polo, navy shorts, navy cap and tartan socks"),
        ("edd-swing-creme-leather", "Man swinging a golf club in the Birdeon men's navy tartan golf polo, cream shorts and cream cap"),
        ("forepack-navy", "Flat lay of the Birdeon men's navy tartan golf polo with navy shorts, navy cap and matching tartan socks"),
    ],
    related=["mens-navy-golf-shorts", "mens-cream-golf-shorts", "navy-golf-cap", "mens-navy-tartan-golf-socks"],
    description=(
        "The men's navy tartan golf polo sits at the centre of Birdeon's Highland Hole Out collection. A deep navy ground is crossed with purple and orange checks, then finished with a solid orange collar, orange sleeve trim and a small leather Birdeon chest tag. The shape is a classic short-sleeve polo, easy to wear tucked or untucked over golf shorts."
        "\n\n"
        "It is shown on the course with navy shorts and a navy cap, and again with cream shorts and a cream cap for a lighter look. Cut with warm-weather rounds in Australia, the Philippines and Taiwan in mind, as well as travel days between them. Fabric details coming soon. This men's golf polo will be available soon."
    ),
)
P(
    slug="mens-navy-golf-shorts",
    name="Men's Navy Golf Shorts",
    short="Clean navy shorts to sit under the tartan polo.",
    catalogue="highland-hole-out",
    group="highland-navy-men",
    kind="Men's golf shorts",
    images=[
        ("edd-forepack-purple-v2", "Man wearing Birdeon navy golf shorts with the navy tartan polo on a golf course"),
        ("forepack-navy", "Flat lay of Birdeon men's navy golf shorts beside the navy tartan polo, cap and socks"),
        ("edd-beach-navy-leather", "Man wearing Birdeon navy golf shorts and the navy tartan polo by the water"),
    ],
    related=["mens-navy-tartan-golf-polo", "navy-golf-cap", "mens-navy-tartan-golf-socks"],
    description=(
        "These men's navy golf shorts are the clean counterpart to the Highland Hole Out tartan polo. The colour is a solid deep navy, with a simple belt loop and a tailored short length that sits neatly on the course or off it."
        "\n\n"
        "Pair them with the navy tartan polo, the navy leather-patch cap and the matching tartan socks for the full navy look. A straightforward short for weekend golf in Australia and further afield. Fabric details coming soon. Coming soon — register your interest and we will let you know when these golf shorts are available."
    ),
)
P(
    slug="mens-cream-golf-shorts",
    name="Men's Cream Golf Shorts",
    short="A lighter short, worn with the navy tartan polo.",
    catalogue="highland-hole-out",
    group="highland-navy-men",
    kind="Men's golf shorts",
    images=[
        ("edd-swing-creme-leather", "Man mid-swing on a palm-lined golf course wearing Birdeon cream golf shorts with the navy tartan polo and a cream cap"),
        ("caps-v2", "Birdeon cream golf cap from the same Highland Hole Out look as the cream golf shorts"),
    ],
    related=["mens-navy-tartan-golf-polo", "cream-golf-cap"],
    description=(
        "The men's cream golf shorts offer a lighter way to wear the navy tartan polo. Shown mid-swing on a palm-lined course, they are a clean, mid-length short with a dark belt, set against navy tartan socks and a cream cap with an orange underside to the brim."
        "\n\n"
        "This colourway is a styling option within Highland Hole Out rather than a separate pattern — cream shorts, cream cap, same tartan polo. A bright-weather choice for golf in warmer parts of Australia, the Philippines and Taiwan. Fabric details coming soon. These golf shorts will be available soon."
    ),
)
P(
    slug="mens-navy-tartan-golf-socks",
    name="Men's Navy Tartan Golf Socks",
    short="Crew socks in the navy, purple and orange tartan.",
    catalogue="highland-hole-out",
    group="highland-navy-men",
    kind="Men's golf socks",
    images=[
        ("forepack-navy", "Flat lay of Birdeon men's navy tartan golf socks with the matching polo, navy shorts and navy cap"),
        ("edd-forepack-purple-v2", "Navy tartan golf socks worn with the Birdeon navy tartan polo and navy shorts"),
        ("edd-swing-creme-leather", "Navy tartan golf socks worn with cream shorts and the navy tartan polo"),
    ],
    related=["mens-navy-tartan-golf-polo", "mens-navy-golf-shorts", "mens-cream-golf-shorts"],
    description=(
        "Men's navy tartan golf socks pick up the same navy, purple and orange check as the Highland Hole Out polo. They are shown as a crew length, worn with both the navy shorts and the cream shorts."
        "\n\n"
        "A small finish that ties the look together on the course. Fabric details coming soon. These golf socks will be available soon."
    ),
)
P(
    slug="mens-black-neon-tartan-golf-polo",
    name="Men's Black Neon Tartan Golf Polo",
    short="Black tartan with neon pink and lime, and a pink collar.",
    catalogue="highland-hole-out",
    group="highland-black-men",
    kind="Men's golf polo",
    images=[
        ("edd-course-black-neon-leather", "Man standing on a tropical golf course wearing the Birdeon men's black neon tartan golf polo, black shorts and black cap"),
        ("forepack-black-neon", "Flat lay of the Birdeon men's black neon tartan golf polo with black shorts, black cap and matching tartan socks"),
    ],
    related=["mens-black-golf-shorts", "black-golf-cap", "mens-black-neon-tartan-golf-socks"],
    description=(
        "The men's black neon tartan golf polo is the bolder half of Highland Hole Out. A black ground is lined with neon pink and lime checks, then cut with a solid neon-pink collar and sleeve trim and a small leather Birdeon chest tag."
        "\n\n"
        "It is a short-sleeve golf polo with a clear, graphic presence on the course — made to be worn with the black shorts, the black leather-patch cap and the matching tartan socks. A strong look for players who want colour in their golf apparel without leaving a classic polo shape. Fabric details coming soon. Coming soon."
    ),
)
P(
    slug="mens-black-golf-shorts",
    name="Men's Black Golf Shorts",
    short="Solid black shorts for the neon tartan polo.",
    catalogue="highland-hole-out",
    group="highland-black-men",
    kind="Men's golf shorts",
    images=[
        ("edd-course-black-neon-leather", "Man wearing Birdeon black golf shorts with the black neon tartan polo on a golf course"),
        ("forepack-black-neon", "Flat lay of Birdeon men's black golf shorts with the black neon tartan polo, cap and socks"),
    ],
    related=["mens-black-neon-tartan-golf-polo", "black-golf-cap", "mens-black-neon-tartan-golf-socks"],
    description=(
        "Men's black golf shorts keep the Highland Hole Out neon tartan polo in check. They are a solid black, tailored short with belt loops, shown as part of the black and neon set."
        "\n\n"
        "Wear them with the black neon tartan polo and the black cap for a complete course look. Fabric details coming soon. These golf shorts will be available soon."
    ),
)
P(
    slug="mens-black-neon-tartan-golf-socks",
    name="Men's Black Neon Tartan Golf Socks",
    short="Crew socks in the black, pink and lime tartan.",
    catalogue="highland-hole-out",
    group="highland-black-men",
    kind="Men's golf socks",
    images=[
        ("forepack-black-neon", "Flat lay of Birdeon men's black neon tartan golf socks with the matching polo, black shorts and black cap"),
    ],
    related=["mens-black-neon-tartan-golf-polo", "mens-black-golf-shorts"],
    description=(
        "These men's golf socks repeat the black, neon pink and lime tartan of the Highland Hole Out polo, in a crew length that sits neatly with the black shorts."
        "\n\n"
        "A matching finish for the black neon look. Fabric details coming soon. Coming soon."
    ),
)

# ---------- Highland women ----------
P(
    slug="womens-navy-tartan-golf-polo",
    name="Women's Navy Tartan Golf Polo",
    short="The navy, purple and orange tartan, cut as a women's polo.",
    catalogue="highland-hole-out",
    group="highland-navy-women",
    kind="Women's golf polo",
    images=[
        ("herrera-reverse-navy", "Woman lining up a putt at sunset in the Birdeon women's navy tartan golf polo, reverse orange tartan skirt, navy cap and tartan socks"),
        ("forepack-women-navy-tartan", "Flat lay of the Birdeon women's navy tartan golf polo with a reverse orange tartan skirt, navy cap and tartan socks"),
    ],
    related=["womens-navy-orange-tartan-golf-skirt", "navy-golf-cap", "womens-navy-tartan-golf-socks"],
    description=(
        "The women's navy tartan golf polo carries the same navy, purple and orange check as the men's Highland Hole Out polo, with an orange collar, orange sleeve trim and a leather Birdeon chest tag. It is cut as a short-sleeve women's golf polo, shown tucked into a reverse-colour tartan skirt."
        "\n\n"
        "In this collection the skirt is the reverse of the shirt — more orange in the check — so the two pieces read as a pair without matching exactly. A considered look for golfers in Australia, the Philippines and Taiwan. Fabric details coming soon. This women's golf polo will be available soon."
    ),
)
P(
    slug="womens-navy-orange-tartan-golf-skirt",
    name="Women's Navy and Orange Tartan Golf Skirt",
    short="A pleated skirt in the reverse of the navy polo.",
    catalogue="highland-hole-out",
    group="highland-navy-women",
    kind="Women's golf skirt",
    images=[
        ("herrera-reverse-navy", "Woman wearing the Birdeon navy and orange reverse tartan pleated golf skirt with the navy tartan polo"),
        ("forepack-women-navy-tartan", "Flat lay of the Birdeon women's navy and orange tartan pleated golf skirt with the matching polo, cap and socks"),
    ],
    related=["womens-navy-tartan-golf-polo", "womens-navy-tartan-golf-socks", "navy-golf-cap"],
    description=(
        "This women's tartan golf skirt is cut in the reverse of the navy polo: the same family of checks, but with orange taking the lead over navy and purple. It is a pleated golf skirt, shown at a mid-thigh length on the course."
        "\n\n"
        "Reverse colour is the idea behind every Highland Hole Out women's set — the shirt and skirt talk to each other rather than repeating the same pattern. Fabric details coming soon. This golf skirt will be available soon."
    ),
)
P(
    slug="womens-navy-tartan-golf-socks",
    name="Women's Navy Tartan Knee-High Golf Socks",
    short="Knee-high socks in the navy tartan.",
    catalogue="highland-hole-out",
    group="highland-navy-women",
    kind="Women's golf socks",
    images=[
        ("herrera-reverse-navy", "Woman wearing Birdeon navy tartan knee-high golf socks with the navy polo and reverse tartan skirt"),
        ("forepack-women-navy-tartan", "Flat lay of Birdeon women's navy tartan golf socks with the polo, skirt and navy cap"),
    ],
    related=["womens-navy-tartan-golf-polo", "womens-navy-orange-tartan-golf-skirt"],
    description=(
        "Women's navy tartan knee-high golf socks complete the Highland Hole Out navy look. They pick up the polo's navy, purple and orange check and are shown worn to the knee with the reverse tartan skirt and white golf shoes."
        "\n\n"
        "Fabric details coming soon. These golf socks will be available soon."
    ),
)
P(
    slug="womens-pink-lemon-tartan-golf-polo",
    name="Women's Pink and Lemon Tartan Golf Polo",
    short="A pink tartan polo with a lemon collar.",
    catalogue="highland-hole-out",
    group="highland-pink-lemon-women",
    kind="Women's golf polo",
    images=[
        ("herrera-reverse-pink-lemon", "Woman on a palm-lined golf course wearing the Birdeon pink and lemon tartan golf polo, lemon reverse tartan skirt, pink cap and pink tartan socks"),
        ("forepack-women-pink-lemon", "Flat lay of the Birdeon women's pink and lemon tartan golf polo with a lemon tartan skirt, pink cap and pink tartan socks"),
    ],
    related=["womens-lemon-tartan-golf-skirt", "pink-golf-cap", "womens-pink-lemon-tartan-golf-socks"],
    description=(
        "The women's pink and lemon tartan golf polo is one of the brighter Highland Hole Out colourways. A pink ground is crossed with lemon and white checks, then finished with a lemon collar, lemon sleeve trim and a leather Birdeon chest tag."
        "\n\n"
        "It is a short-sleeve women's golf polo, shown with a lemon tartan pleated skirt — the reverse of the shirt — a pink cap and matching socks. Made for warm, high-colour days on the course. Fabric details coming soon. Coming soon."
    ),
)
P(
    slug="womens-lemon-tartan-golf-skirt",
    name="Women's Lemon Tartan Golf Skirt",
    short="A pleated lemon tartan skirt, the reverse of the pink polo.",
    catalogue="highland-hole-out",
    group="highland-pink-lemon-women",
    kind="Women's golf skirt",
    images=[
        ("herrera-reverse-pink-lemon", "Woman wearing the Birdeon lemon tartan pleated golf skirt with the pink and lemon polo"),
        ("forepack-women-pink-lemon", "Flat lay of the Birdeon women's lemon tartan pleated golf skirt with the pink lemon polo, pink cap and socks"),
    ],
    related=["womens-pink-lemon-tartan-golf-polo", "womens-pink-lemon-tartan-golf-socks", "pink-golf-cap"],
    description=(
        "This women's lemon tartan golf skirt reverses the pink and lemon polo: a lemon ground with pink and white checks, cut as a pleated golf skirt. Worn together, the two pieces feel matched without being identical."
        "\n\n"
        "A bright golf skirt for Highland Hole Out. Fabric details coming soon. This golf skirt will be available soon."
    ),
)
P(
    slug="womens-pink-lemon-tartan-golf-socks",
    name="Women's Pink and Lemon Tartan Knee-High Golf Socks",
    short="Knee-high socks in the pink and lemon tartan.",
    catalogue="highland-hole-out",
    group="highland-pink-lemon-women",
    kind="Women's golf socks",
    images=[
        ("herrera-reverse-pink-lemon", "Woman wearing Birdeon pink and lemon tartan knee-high golf socks with the matching polo and skirt"),
        ("forepack-women-pink-lemon", "Flat lay of Birdeon women's pink and lemon tartan golf socks with the polo, skirt and pink cap"),
    ],
    related=["womens-pink-lemon-tartan-golf-polo", "womens-lemon-tartan-golf-skirt"],
    description=(
        "Women's pink and lemon tartan knee-high golf socks follow the polo's check, in a knee-high length worn with the lemon reverse skirt."
        "\n\n"
        "Fabric details coming soon. Coming soon."
    ),
)
P(
    slug="womens-lemon-lime-tartan-golf-polo",
    name="Women's Lemon and Lime Tartan Golf Polo",
    short="A yellow tartan polo with a lime collar.",
    catalogue="highland-hole-out",
    group="highland-lemon-lime-women",
    kind="Women's golf polo",
    images=[
        ("herrera-reverse-lemon-lime", "Woman walking a palm-lined fairway in the Birdeon lemon and lime tartan golf polo, lime reverse tartan skirt, lemon cap and lemon tartan socks"),
        ("forepack-women-lemon-lime", "Flat lay of the Birdeon women's lemon and lime tartan golf polo with a lime tartan skirt, lemon cap and lemon tartan socks"),
    ],
    related=["womens-lime-tartan-golf-skirt", "lemon-golf-cap", "womens-lemon-lime-tartan-golf-socks"],
    description=(
        "The women's lemon and lime tartan golf polo is a high-summer colourway in Highland Hole Out. A yellow ground is crossed with lime and white checks, with a lime collar, lime sleeve trim and a leather Birdeon chest tag."
        "\n\n"
        "It is shown as a short-sleeve women's golf polo with a lime tartan pleated skirt, a lemon cap and matching socks — a clear, sunny look for warm-weather golf. Fabric details coming soon. This women's golf polo will be available soon."
    ),
)
P(
    slug="womens-lime-tartan-golf-skirt",
    name="Women's Lime Tartan Golf Skirt",
    short="A pleated lime tartan skirt, the reverse of the lemon polo.",
    catalogue="highland-hole-out",
    group="highland-lemon-lime-women",
    kind="Women's golf skirt",
    images=[
        ("herrera-reverse-lemon-lime", "Woman wearing the Birdeon lime tartan pleated golf skirt with the lemon and lime polo"),
        ("forepack-women-lemon-lime", "Flat lay of the Birdeon women's lime tartan pleated golf skirt with the lemon lime polo, lemon cap and socks"),
    ],
    related=["womens-lemon-lime-tartan-golf-polo", "womens-lemon-lime-tartan-golf-socks", "lemon-golf-cap"],
    description=(
        "This women's lime tartan golf skirt is the reverse of the lemon and lime polo: a lime ground with yellow and white checks, cut as a pleated golf skirt."
        "\n\n"
        "Worn with the lemon polo it completes one of Highland Hole Out's brightest sets. Fabric details coming soon. This golf skirt will be available soon."
    ),
)
P(
    slug="womens-lemon-lime-tartan-golf-socks",
    name="Women's Lemon and Lime Tartan Knee-High Golf Socks",
    short="Knee-high socks in the lemon and lime tartan.",
    catalogue="highland-hole-out",
    group="highland-lemon-lime-women",
    kind="Women's golf socks",
    images=[
        ("herrera-reverse-lemon-lime", "Woman wearing Birdeon lemon and lime tartan knee-high golf socks with the matching polo and skirt"),
        ("forepack-women-lemon-lime", "Flat lay of Birdeon women's lemon and lime tartan golf socks with the polo, skirt and lemon cap"),
    ],
    related=["womens-lemon-lime-tartan-golf-polo", "womens-lime-tartan-golf-skirt"],
    description=(
        "Women's lemon and lime tartan knee-high golf socks repeat the polo's yellow, lime and white check, worn to the knee with the lime reverse skirt."
        "\n\n"
        "Fabric details coming soon. Coming soon."
    ),
)
P(
    slug="womens-pink-purple-tartan-golf-polo",
    name="Women's Pink and Purple Tartan Golf Polo",
    short="A pink tartan polo with a purple collar.",
    catalogue="highland-hole-out",
    group="highland-pink-purple-women",
    kind="Women's golf polo",
    images=[
        ("herrera-reverse-pink-purple", "Woman mid-swing in the Birdeon pink and purple tartan golf polo, purple reverse tartan skirt, purple cap and pink tartan socks"),
        ("forepack-women-pink-purple", "Flat lay of the Birdeon women's pink and purple tartan golf polo with a purple tartan skirt, pink cap and pink tartan socks"),
    ],
    related=["womens-purple-tartan-golf-skirt", "purple-golf-cap", "pink-golf-cap", "womens-pink-purple-tartan-golf-socks"],
    description=(
        "The women's pink and purple tartan golf polo closes Highland Hole Out's brighter colourways. A pink ground is crossed with purple and white checks, with a purple collar, purple sleeve trim and a leather Birdeon chest tag."
        "\n\n"
        "It is a short-sleeve women's golf polo, shown with a purple tartan pleated skirt and pink tartan socks. The worn look is styled with a purple cap; the flat lay shows a pink cap from the same collection. Fabric details coming soon. This women's golf polo will be available soon."
    ),
)
P(
    slug="womens-purple-tartan-golf-skirt",
    name="Women's Purple Tartan Golf Skirt",
    short="A pleated purple tartan skirt, the reverse of the pink polo.",
    catalogue="highland-hole-out",
    group="highland-pink-purple-women",
    kind="Women's golf skirt",
    images=[
        ("herrera-reverse-pink-purple", "Woman wearing the Birdeon purple tartan pleated golf skirt with the pink and purple polo"),
        ("forepack-women-pink-purple", "Flat lay of the Birdeon women's purple tartan pleated golf skirt with the pink purple polo, cap and socks"),
    ],
    related=["womens-pink-purple-tartan-golf-polo", "womens-pink-purple-tartan-golf-socks", "purple-golf-cap"],
    description=(
        "This women's purple tartan golf skirt reverses the pink and purple polo: a purple ground with pink and white checks, cut as a pleated golf skirt."
        "\n\n"
        "A rich, graphic golf skirt for Highland Hole Out. Fabric details coming soon. This golf skirt will be available soon."
    ),
)
P(
    slug="womens-pink-purple-tartan-golf-socks",
    name="Women's Pink and Purple Tartan Knee-High Golf Socks",
    short="Knee-high socks in the pink and purple tartan.",
    catalogue="highland-hole-out",
    group="highland-pink-purple-women",
    kind="Women's golf socks",
    images=[
        ("herrera-reverse-pink-purple", "Woman wearing Birdeon pink and purple tartan knee-high golf socks with the matching polo and skirt"),
        ("forepack-women-pink-purple", "Flat lay of Birdeon women's pink and purple tartan golf socks with the polo, skirt and cap"),
    ],
    related=["womens-pink-purple-tartan-golf-polo", "womens-purple-tartan-golf-skirt"],
    description=(
        "Women's pink and purple tartan knee-high golf socks follow the polo's check and are shown worn to the knee with the purple reverse skirt."
        "\n\n"
        "Fabric details coming soon. Coming soon."
    ),
)

# ---------- Caps and bag ----------
P(
    slug="navy-golf-cap",
    name="Navy Golf Cap",
    short="A navy cap with a leather Birdeon patch and tartan trim under the brim.",
    catalogue="highland-hole-out",
    group="caps",
    kind="Golf cap",
    also_on=["winter-league"],
    images=[
        ("caps-v2", "Navy Birdeon golf cap with a leather bird-and-wordmark patch and tartan underside, shown beside black and cream caps"),
        ("forepack-navy", "Navy Birdeon golf cap in the men's navy Highland Hole Out flat lay"),
        ("edd-beach-navy-leather", "Navy Birdeon golf cap worn with the men's navy tartan polo on a beach"),
        ("winter-forepack-men", "Navy Birdeon golf cap shown with the Winter League men's set"),
    ],
    related=["black-golf-cap", "cream-golf-cap", "mens-navy-tartan-golf-polo"],
    description=(
        "The navy golf cap is a structured six-panel cap in deep navy, finished with a brown leather patch of the Birdeon bird and wordmark. The underside of the brim is trimmed in the navy, purple and orange tartan."
        "\n\n"
        "It appears throughout Highland Hole Out — with the men's navy set and the women's navy set — and again in the Winter League flat lays. A simple cap for the course and travel days. Fabric details coming soon. This golf cap will be available soon."
    ),
)
P(
    slug="black-golf-cap",
    name="Black Golf Cap",
    short="A black cap with a leather Birdeon patch and neon pink trim under the brim.",
    catalogue="highland-hole-out",
    group="caps",
    kind="Golf cap",
    images=[
        ("caps-v2", "Black Birdeon golf cap with a leather patch and neon pink underside, shown beside navy and cream caps"),
        ("forepack-black-neon", "Black Birdeon golf cap in the men's black neon Highland Hole Out flat lay"),
        ("edd-course-black-neon-leather", "Black Birdeon golf cap worn with the men's black neon tartan polo on a golf course"),
    ],
    related=["navy-golf-cap", "cream-golf-cap", "mens-black-neon-tartan-golf-polo"],
    description=(
        "The black golf cap matches the Highland Hole Out neon tartan look. It is a structured cap in solid black, with a brown leather Birdeon patch and a neon pink underside to the brim."
        "\n\n"
        "Wear it with the black neon tartan polo and black shorts. Fabric details coming soon. This golf cap will be available soon."
    ),
)
P(
    slug="cream-golf-cap",
    name="Cream Golf Cap",
    short="A cream cap with a leather Birdeon patch and orange trim under the brim.",
    catalogue="highland-hole-out",
    group="caps",
    kind="Golf cap",
    images=[
        ("caps-v2", "Cream Birdeon golf cap with a leather patch and orange underside, shown beside navy and black caps"),
        ("edd-swing-creme-leather", "Cream Birdeon golf cap worn with the navy tartan polo and cream shorts during a golf swing"),
    ],
    related=["navy-golf-cap", "black-golf-cap", "mens-cream-golf-shorts"],
    description=(
        "The cream golf cap is the light option in the Highland Hole Out cap set. It is a structured cream cap with a brown leather Birdeon patch and an orange underside to the brim."
        "\n\n"
        "It is shown worn with the navy tartan polo and cream golf shorts. Fabric details coming soon. This golf cap will be available soon."
    ),
)
P(
    slug="pink-golf-cap",
    name="Pink Golf Cap",
    short="A pink cap with a leather Birdeon patch.",
    catalogue="highland-hole-out",
    group="caps",
    kind="Golf cap",
    images=[
        ("herrera-reverse-pink-lemon", "Pink Birdeon golf cap worn with the women's pink and lemon tartan golf polo and skirt"),
        ("forepack-women-pink-lemon", "Pink Birdeon golf cap in the women's pink and lemon Highland Hole Out flat lay"),
        ("forepack-women-pink-purple", "Pink Birdeon golf cap shown in the women's pink and purple flat lay"),
    ],
    related=["womens-pink-lemon-tartan-golf-polo", "lemon-golf-cap", "purple-golf-cap"],
    description=(
        "The pink golf cap is a structured cap in a soft pink, finished with a brown leather Birdeon patch. It is shown with the women's pink and lemon tartan set, and also appears in the pink and purple flat lay."
        "\n\n"
        "A bright cap for Highland Hole Out. Fabric details coming soon. Coming soon."
    ),
)
P(
    slug="lemon-golf-cap",
    name="Lemon Golf Cap",
    short="A lemon cap with a leather Birdeon patch.",
    catalogue="highland-hole-out",
    group="caps",
    kind="Golf cap",
    images=[
        ("herrera-reverse-lemon-lime", "Lemon Birdeon golf cap worn with the women's lemon and lime tartan golf polo and skirt"),
        ("forepack-women-lemon-lime", "Lemon Birdeon golf cap in the women's lemon and lime Highland Hole Out flat lay"),
    ],
    related=["womens-lemon-lime-tartan-golf-polo", "pink-golf-cap"],
    description=(
        "The lemon golf cap is a structured yellow cap with a brown leather Birdeon patch, shown with the women's lemon and lime tartan set in Highland Hole Out."
        "\n\n"
        "Fabric details coming soon. This golf cap will be available soon."
    ),
)
P(
    slug="purple-golf-cap",
    name="Purple Golf Cap",
    short="A purple cap with a leather Birdeon patch.",
    catalogue="highland-hole-out",
    group="caps",
    kind="Golf cap",
    images=[
        ("herrera-reverse-pink-purple", "Purple Birdeon golf cap worn with the women's pink and purple tartan golf polo and skirt"),
    ],
    related=["womens-pink-purple-tartan-golf-polo", "pink-golf-cap"],
    description=(
        "The purple golf cap is a structured cap in a vivid purple, finished with a brown leather Birdeon patch. It is shown on the course with the women's pink and purple tartan set."
        "\n\n"
        "Fabric details coming soon. Coming soon."
    ),
)
P(
    slug="navy-tartan-golf-bag",
    name="Navy Tartan Golf Bag",
    short="A navy and orange tartan stand bag with the printed Birdeon logo.",
    catalogue="highland-hole-out",
    group="bag",
    kind="Golf bag",
    images=[
        ("bag-navy-logo", "Birdeon navy and orange tartan golf stand bag with the printed full-colour bird logo and Birdeon wordmark, orange trim and matching headcovers"),
    ],
    related=["mens-navy-tartan-golf-polo", "womens-navy-tartan-golf-polo", "navy-golf-cap"],
    description=(
        "The navy tartan golf bag carries Highland Hole Out onto the fairway. It is a stand bag in navy, orange and purple tartan, with orange trim, a black stand and matching tartan headcovers. The full-colour Birdeon bird and wordmark are printed on the side of the bag."
        "\n\n"
        "Designed as a companion to the navy tartan apparel, for golf at home in Australia or on the road. Further construction details coming soon. This golf bag will be available soon."
    ),
)

print("highland done", len(PRODUCTS))

# ---------- Winter ----------
P(
    slug="mens-forest-golf-quarter-zip",
    name="Men's Forest Golf Quarter-Zip",
    short="A forest green quarter-zip to layer over the winter polo.",
    catalogue="winter-league",
    group="winter-men",
    kind="Men's golf quarter-zip",
    images=[
        ("winter-edd-course", "Man on an autumn golf course wearing the Birdeon forest green quarter-zip over a polo, with charcoal golf trousers and a navy cap"),
        ("winter-forepack-men", "Flat lay of the Birdeon forest green golf quarter-zip with a navy tartan polo, charcoal trousers, navy cap and burgundy tartan socks"),
    ],
    related=["mens-winter-navy-tartan-golf-polo", "mens-charcoal-golf-trousers", "navy-golf-cap"],
    description=(
        "The men's forest golf quarter-zip is the layering piece in Birdeon's Winter League collection. It is a deep forest green, with a short zip at the neck and a small leather Birdeon tag on the chest, shown worn over a polo on a cooler course."
        "\n\n"
        "Pair it with the charcoal golf trousers and the navy tartan polo underneath. A darker, quieter look than Highland Hole Out, for rounds when the air has a bit of bite. Fabric details coming soon. This quarter-zip will be available soon."
    ),
)
P(
    slug="mens-winter-navy-tartan-golf-polo",
    name="Men's Winter Navy Tartan Golf Polo",
    short="A darker navy tartan polo to wear under the quarter-zip.",
    catalogue="winter-league",
    group="winter-men",
    kind="Men's golf polo",
    images=[
        ("winter-forepack-men", "Flat lay of the Birdeon men's winter navy tartan golf polo with forest quarter-zip, charcoal trousers, navy cap and burgundy tartan socks"),
        ("winter-edd-course", "Man wearing the Winter League layering look; the navy tartan polo sits under the forest quarter-zip"),
    ],
    related=["mens-forest-golf-quarter-zip", "mens-charcoal-golf-trousers", "mens-burgundy-tartan-golf-socks"],
    description=(
        "The men's winter navy tartan golf polo is a darker check than Highland Hole Out: a navy ground with burgundy and forest lines, and a navy collar. It is the polo meant to sit under the forest quarter-zip, or to be worn on its own."
        "\n\n"
        "The worn course shot shows the polo mostly covered by the quarter-zip, so the tartan is clearest in the flat lay. Fabric details coming soon. This men's golf polo will be available soon."
    ),
)
P(
    slug="mens-charcoal-golf-trousers",
    name="Men's Charcoal Golf Trousers",
    short="Full-length charcoal trousers for Winter League.",
    catalogue="winter-league",
    group="winter-men",
    kind="Men's golf trousers",
    images=[
        ("winter-edd-course", "Man wearing Birdeon charcoal full-length golf trousers with the forest quarter-zip on an autumn course"),
        ("winter-forepack-men", "Flat lay of Birdeon men's charcoal golf trousers with the winter polo, quarter-zip, cap and socks"),
    ],
    related=["mens-forest-golf-quarter-zip", "mens-winter-navy-tartan-golf-polo"],
    description=(
        "Men's charcoal golf trousers are the bottom half of Winter League. They are full-length, in a solid charcoal, cut as a clean golf trouser rather than a short — for cooler mornings and winter competitions."
        "\n\n"
        "Shown with the forest quarter-zip and navy tartan polo. A straightforward trouser for golf in cooler Australian conditions, and for travel to courses that need a longer layer. Fabric details coming soon. These golf trousers will be available soon."
    ),
)
P(
    slug="mens-burgundy-tartan-golf-socks",
    name="Men's Burgundy Tartan Golf Socks",
    short="Crew socks in a burgundy tartan.",
    catalogue="winter-league",
    group="winter-men",
    kind="Men's golf socks",
    images=[
        ("winter-forepack-men", "Flat lay of Birdeon men's burgundy tartan golf socks with the Winter League polo, trousers, quarter-zip and navy cap"),
    ],
    related=["mens-winter-navy-tartan-golf-polo", "mens-charcoal-golf-trousers"],
    description=(
        "Men's burgundy tartan golf socks pick up the darker red in the Winter League polo. They are shown as a crew length in the men's flat lay, beside the charcoal trousers and forest quarter-zip."
        "\n\n"
        "Fabric details coming soon. Coming soon."
    ),
)
P(
    slug="womens-winter-burgundy-tartan-golf-polo",
    name="Women's Winter Burgundy Tartan Golf Polo",
    short="A burgundy tartan polo with a burgundy collar.",
    catalogue="winter-league",
    group="winter-women",
    kind="Women's golf polo",
    images=[
        ("winter-herrera", "Woman lining up a putt at dusk in the Birdeon women's winter burgundy tartan golf polo, forest tartan skirt, burgundy cap and burgundy socks"),
        ("winter-forepack-women", "Flat lay of the Birdeon women's burgundy tartan golf polo with a forest tartan skirt, navy cap and burgundy socks"),
    ],
    related=["womens-winter-forest-tartan-golf-skirt", "womens-burgundy-golf-socks", "burgundy-golf-cap"],
    description=(
        "The women's winter burgundy tartan golf polo is a darker, quieter colourway for Winter League. A burgundy ground is crossed with navy and forest checks, with a burgundy collar and a leather Birdeon chest tag. It is cut as a short-sleeve women's golf polo."
        "\n\n"
        "It is shown with a forest tartan pleated skirt — the reverse of the shirt — and burgundy socks. A composed look for cooler late-afternoon rounds. Fabric details coming soon. This women's golf polo will be available soon."
    ),
)
P(
    slug="womens-winter-forest-tartan-golf-skirt",
    name="Women's Winter Forest Tartan Golf Skirt",
    short="A pleated forest tartan skirt, the reverse of the burgundy polo.",
    catalogue="winter-league",
    group="winter-women",
    kind="Women's golf skirt",
    images=[
        ("winter-herrera", "Woman wearing the Birdeon forest tartan pleated golf skirt with the winter burgundy polo"),
        ("winter-forepack-women", "Flat lay of the Birdeon women's forest tartan pleated golf skirt with the burgundy polo, cap and socks"),
    ],
    related=["womens-winter-burgundy-tartan-golf-polo", "womens-burgundy-golf-socks", "burgundy-golf-cap"],
    description=(
        "This women's forest tartan golf skirt is the reverse of the winter burgundy polo: a forest green ground with burgundy and navy checks, cut as a pleated golf skirt."
        "\n\n"
        "It keeps the Highland idea of a reverse-colour skirt, in a darker Winter League palette. Fabric details coming soon. This golf skirt will be available soon."
    ),
)
P(
    slug="womens-burgundy-golf-socks",
    name="Women's Burgundy Knee-High Golf Socks",
    short="Solid burgundy knee-high socks.",
    catalogue="winter-league",
    group="winter-women",
    kind="Women's golf socks",
    images=[
        ("winter-herrera", "Woman wearing Birdeon burgundy knee-high golf socks with the winter polo and forest tartan skirt"),
        ("winter-forepack-women", "Flat lay of Birdeon women's burgundy golf socks with the winter polo, skirt and cap"),
    ],
    related=["womens-winter-burgundy-tartan-golf-polo", "womens-winter-forest-tartan-golf-skirt"],
    description=(
        "Women's burgundy knee-high golf socks are a solid ribbed sock, shown to the knee with the Winter League polo and forest tartan skirt."
        "\n\n"
        "Fabric details coming soon. Coming soon."
    ),
)
P(
    slug="burgundy-golf-cap",
    name="Burgundy Golf Cap",
    short="A burgundy cap with a leather Birdeon patch.",
    catalogue="winter-league",
    group="winter-women",
    kind="Golf cap",
    images=[
        ("winter-herrera", "Burgundy Birdeon golf cap worn with the women's Winter League tartan polo and forest tartan skirt"),
    ],
    related=["womens-winter-burgundy-tartan-golf-polo", "navy-golf-cap"],
    description=(
        "The burgundy golf cap is a structured cap in a deep burgundy, finished with a brown leather Birdeon patch. It is shown worn with the women's Winter League set. The women's flat lay also includes the navy golf cap as an alternative."
        "\n\n"
        "Fabric details coming soon. This golf cap will be available soon."
    ),
)

# ---------- Summer ----------
P(
    slug="mens-coral-golf-polo",
    name="Men's Coral Golf Polo",
    short="A plain coral polo with aqua collar and trim.",
    catalogue="summer-links",
    group="summer-men",
    kind="Men's golf polo",
    images=[
        ("summer-edd-course", "Man on a links-style course wearing the Birdeon men's coral golf polo, aqua shorts and a coral cap"),
        ("summer-forepack-men", "Flat lay of the Birdeon men's coral golf polo with aqua shorts, coral cap and aqua socks"),
    ],
    related=["mens-aqua-golf-shorts", "coral-golf-cap", "aqua-golf-socks"],
    description=(
        "The men's coral golf polo is the lead piece in Birdeon's Summer Links collection — bright, plain colour rather than tartan. The body is a clean coral, with an aqua collar, aqua sleeve trim and a small leather Birdeon chest tag."
        "\n\n"
        "It is a short-sleeve golf polo, shown with aqua shorts and a coral cap on a links-style course. Cut for warm-weather golf in Australia, the Philippines and Taiwan. Fabric details coming soon. This men's golf polo will be available soon."
    ),
)
P(
    slug="mens-aqua-golf-shorts",
    name="Men's Aqua Golf Shorts",
    short="Solid aqua shorts to sit under the coral polo.",
    catalogue="summer-links",
    group="summer-men",
    kind="Men's golf shorts",
    images=[
        ("summer-edd-course", "Man wearing Birdeon aqua golf shorts with the coral polo on a links-style course"),
        ("summer-forepack-men", "Flat lay of Birdeon men's aqua golf shorts with the coral polo, coral cap and aqua socks"),
    ],
    related=["mens-coral-golf-polo", "coral-golf-cap", "aqua-golf-socks"],
    description=(
        "Men's aqua golf shorts are a solid, bright short for Summer Links, shown with the coral polo. They have a clean, tailored short shape with belt loops, in a clear aqua that stands up to the polo's coral."
        "\n\n"
        "A warm-weather golf short for coastal and inland courses. Fabric details coming soon. These golf shorts will be available soon."
    ),
)
P(
    slug="coral-golf-cap",
    name="Coral Golf Cap",
    short="A coral cap with a leather Birdeon patch.",
    catalogue="summer-links",
    group="summer-men",
    kind="Golf cap",
    images=[
        ("summer-edd-course", "Coral Birdeon golf cap worn with the men's coral polo and aqua shorts"),
        ("summer-forepack-men", "Coral Birdeon golf cap in the men's Summer Links flat lay"),
    ],
    related=["mens-coral-golf-polo", "aqua-golf-cap"],
    description=(
        "The coral golf cap is a structured cap in the same coral as the men's Summer Links polo, finished with a brown leather Birdeon patch."
        "\n\n"
        "Fabric details coming soon. This golf cap will be available soon."
    ),
)
P(
    slug="aqua-golf-socks",
    name="Aqua Golf Socks",
    short="Solid aqua socks, shown with both Summer Links sets.",
    catalogue="summer-links",
    group="summer-shared",
    kind="Golf socks",
    images=[
        ("summer-forepack-men", "Aqua golf socks in the Birdeon men's Summer Links flat lay, with the coral polo and aqua shorts"),
        ("summer-forepack-women", "Aqua golf socks in the Birdeon women's Summer Links flat lay, with the aqua polo and coral skirt"),
        ("summer-herrera", "Aqua knee-high golf socks worn with the women's Summer Links polo and coral skirt"),
    ],
    related=["mens-coral-golf-polo", "womens-aqua-golf-polo"],
    description=(
        "Aqua golf socks are a solid, bright sock for Summer Links. They appear as a crew length in the men's set and as a knee-high sock in the women's set, in the same aqua as the men's shorts and the women's polo."
        "\n\n"
        "Fabric details coming soon. Coming soon."
    ),
)
P(
    slug="womens-aqua-golf-polo",
    name="Women's Aqua Golf Polo",
    short="A plain aqua polo with a coral collar.",
    catalogue="summer-links",
    group="summer-women",
    kind="Women's golf polo",
    images=[
        ("summer-herrera", "Woman on a palm-lined golf course wearing the Birdeon women's aqua golf polo, coral pleated skirt, aqua cap and aqua socks"),
        ("summer-forepack-women", "Flat lay of the Birdeon women's aqua golf polo with a coral pleated skirt, aqua cap and aqua socks"),
    ],
    related=["womens-coral-golf-skirt", "aqua-golf-cap", "aqua-golf-socks"],
    description=(
        "The women's aqua golf polo is the plain-colour polo in Summer Links. The body is a clean aqua, with a coral collar, coral sleeve trim and a leather Birdeon chest tag, cut as a short-sleeve women's golf polo."
        "\n\n"
        "It is shown with a coral pleated golf skirt — a reverse of the men's coral-polo-and-aqua-shorts idea — plus an aqua cap and aqua socks. Made for bright, warm rounds. Fabric details coming soon. This women's golf polo will be available soon."
    ),
)
P(
    slug="womens-coral-golf-skirt",
    name="Women's Coral Golf Skirt",
    short="A plain coral pleated golf skirt.",
    catalogue="summer-links",
    group="summer-women",
    kind="Women's golf skirt",
    images=[
        ("summer-herrera", "Woman wearing the Birdeon coral pleated golf skirt with the aqua polo"),
        ("summer-forepack-women", "Flat lay of the Birdeon women's coral pleated golf skirt with the aqua polo, aqua cap and socks"),
    ],
    related=["womens-aqua-golf-polo", "aqua-golf-cap", "aqua-golf-socks"],
    description=(
        "This women's coral golf skirt is a plain, pleated skirt in the same coral used on the men's Summer Links polo. Worn with the aqua women's polo, it keeps the collection's two colours in play without a pattern."
        "\n\n"
        "A bright golf skirt for warm-weather courses. Fabric details coming soon. This golf skirt will be available soon."
    ),
)
P(
    slug="aqua-golf-cap",
    name="Aqua Golf Cap",
    short="An aqua cap with a leather Birdeon patch.",
    catalogue="summer-links",
    group="summer-women",
    kind="Golf cap",
    images=[
        ("summer-herrera", "Aqua Birdeon golf cap worn with the women's aqua polo and coral skirt"),
        ("summer-forepack-women", "Aqua Birdeon golf cap in the women's Summer Links flat lay"),
    ],
    related=["womens-aqua-golf-polo", "coral-golf-cap"],
    description=(
        "The aqua golf cap is a structured cap in the same aqua as the women's Summer Links polo, finished with a brown leather Birdeon patch."
        "\n\n"
        "Fabric details coming soon. This golf cap will be available soon."
    ),
)

BY_SLUG = {p["slug"]: p for p in PRODUCTS}
print("products", len(PRODUCTS))


def by_catalogue(slug: str) -> list[dict]:
    out = []
    for p in PRODUCTS:
        cats = [p["catalogue"]] + p.get("also_on", [])
        if slug in cats:
            out.append(p)
    return out


def prefix(depth: int) -> str:
    return "" if depth == 0 else "../" * depth


def img_size(stem: str) -> tuple[int, int]:
    key = f"products/{stem}.jpg"
    if key in SIZES:
        return tuple(SIZES[key])
    return (1024, 1024)


def picture(stem: str, alt: str, prefix_assets: str, *, lazy=True, class_name="", id_name="", extra_img="") -> str:
    w, h = img_size(stem)
    src = f"{prefix_assets}assets/images/products/{stem}.jpg"
    webp = f"{prefix_assets}assets/images/products/{stem}.webp"
    loading = ' loading="lazy" decoding="async"' if lazy else ' fetchpriority="high" decoding="async"'
    cls = f' class="{class_name}"' if class_name else ""
    ida = f' id="{id_name}"' if id_name else ""
    return (
        f'<picture{cls}>'
        f'<source type="image/webp" srcset="{webp}">'
        f'<img src="{src}" width="{w}" height="{h}" alt="{escape(alt)}"{loading}{ida}{extra_img}>'
        f"</picture>"
    )


def org_ld() -> dict:
    return {
        "@type": "Organization",
        "@id": f"{SITE}/#organization",
        "name": "Birdeon",
        "url": SITE,
        "logo": f"{SITE}/assets/images/logo-birdeon-square.jpg",
        "description": "Birdeon is a golf apparel brand creating tartan and plain-colour golf clothing for players in Australia, the Philippines and Taiwan. Products coming soon.",
        "founders": [
            {"@type": "Person", "name": "Damien Mueller"},
            {"@type": "Person", "name": "Edd Adair"},
        ],
    }


def json_ld(data) -> str:
    return (
        '<script type="application/ld+json">'
        + json.dumps(data, ensure_ascii=False, indent=2)
        + "</script>"
    )


def head(*, title, description, canonical, depth, og_type="website", og_image=None, og_alt=None, extra_ld=None, extra=""):
    p = prefix(depth)
    og_image = og_image or f"{SITE}/assets/images/og-default.jpg"
    og_alt = og_alt or "Birdeon golf apparel logo, coming soon"
    graph = [org_ld()]
    if extra_ld:
        if isinstance(extra_ld, list):
            graph.extend(extra_ld)
        else:
            graph.append(extra_ld)
    ld = {"@context": "https://schema.org", "@graph": graph}
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>{escape(title)}</title>
  <meta name="description" content="{escape(description)}">
  <link rel="canonical" href="{canonical}">
  <meta name="theme-color" content="#000926">
  <meta property="og:type" content="{og_type}">
  <meta property="og:site_name" content="Birdeon">
  <meta property="og:locale" content="en_AU">
  <meta property="og:title" content="{escape(title)}">
  <meta property="og:description" content="{escape(description)}">
  <meta property="og:url" content="{canonical}">
  <meta property="og:image" content="{og_image}">
  <meta property="og:image:alt" content="{escape(og_alt)}">
  <meta name="twitter:card" content="summary_large_image">
  <meta name="twitter:title" content="{escape(title)}">
  <meta name="twitter:description" content="{escape(description)}">
  <meta name="twitter:image" content="{og_image}">
  <link rel="icon" href="{p}assets/icons/favicon-32.png" type="image/png" sizes="32x32">
  <link rel="icon" href="{p}assets/icons/favicon-16.png" type="image/png" sizes="16x16">
  <link rel="apple-touch-icon" href="{p}assets/icons/apple-touch-icon.png">
  <link rel="manifest" href="{p}site.webmanifest">
  <link rel="stylesheet" href="{p}assets/css/fonts.css">
  <link rel="stylesheet" href="{p}assets/css/styles.css">
  {json_ld(ld)}
  {extra}
</head>
"""


def header(depth: int, current: str) -> str:
    p = prefix(depth)
    def cur(key):
        return ' aria-current="page"' if current == key else ""
    return f"""<body>
  <a class="skip" href="#main">Skip to content</a>
  <header class="site-header">
    <div class="wrap header-inner">
      <a class="logo" href="{p}index.html">
        <img src="{p}assets/images/logo-nav.png" width="1147" height="256" alt="Birdeon">
      </a>
      <button class="menu-toggle" type="button" data-nav-toggle aria-expanded="false" aria-controls="site-nav" aria-label="Open menu"><span></span></button>
      <nav class="nav" id="site-nav" data-nav>
        <a href="{p}index.html"{cur("home")}>Home</a>
        <div class="nav-drop" data-drop>
          <button type="button" aria-expanded="false" aria-haspopup="true">Catalogues</button>
          <div class="nav-drop-menu">
            <a href="{p}catalogues/highland-hole-out.html"{cur("highland-hole-out")}">Highland Hole Out<small>Tartan golf apparel</small></a>
            <a href="{p}catalogues/winter-league.html"{cur("winter-league")}">Winter League<small>Trousers and layers</small></a>
            <a href="{p}catalogues/summer-links.html"{cur("summer-links")}">Summer Links<small>Coral and aqua</small></a>
          </div>
        </div>
        <a href="{p}about.html"{cur("about")}>About</a>
        <a href="{p}contact.html"{cur("contact")}>Contact</a>
      </nav>
      <div class="header-cta">
        <button class="btn btn-orange btn-sm" type="button" data-open-notify>Notify me</button>
      </div>
    </div>
  </header>
"""


def footer(depth: int) -> str:
    p = prefix(depth)
    return f"""  <footer class="site-footer">
    <div class="wrap footer-grid">
      <div class="footer-brand">
        <a href="{p}index.html"><img src="{p}assets/images/logo-nav.png" width="1147" height="256" alt="Birdeon"></a>
        <p>Golf apparel by Damien Mueller and Edd Adair. Three catalogues, coming soon.</p>
      </div>
      <div>
        <h2>Catalogues</h2>
        <ul>
          <li><a href="{p}catalogues/highland-hole-out.html">Highland Hole Out</a></li>
          <li><a href="{p}catalogues/winter-league.html">Winter League</a></li>
          <li><a href="{p}catalogues/summer-links.html">Summer Links</a></li>
        </ul>
      </div>
      <div>
        <h2>Birdeon</h2>
        <ul>
          <li><a href="{p}about.html">About</a></li>
          <li><a href="{p}contact.html">Contact</a></li>
          <li><a href="{p}index.html#notify">Notify me</a></li>
        </ul>
      </div>
      <div>
        <h2>Soon</h2>
        <p>Products are not yet for sale. No prices, cart or checkout on this preview. A shop will follow on Shopify.</p>
      </div>
    </div>
    <div class="wrap footer-base">
      <span>&copy; 2026 Birdeon. All rights reserved.</span>
      <span>Australia · Philippines · Taiwan</span>
    </div>
  </footer>
  <div class="modal" id="notify-modal" aria-hidden="true" role="dialog" aria-labelledby="notify-title">
    <div class="modal-backdrop" data-close-modal></div>
    <div class="modal-card">
      <button class="modal-close" type="button" data-close-modal aria-label="Close">&times;</button>
      <h2 id="notify-title" data-notify-title>Notify me when Birdeon is available</h2>
      <p class="muted">Leave your email and we will let you know when this is available. This preview does not store or send your address yet.</p>
      <!-- Visual only: this form has no backend and does not store or send email addresses. -->
      <form class="notify-form" data-visual-form action="#" method="post">
        <input type="hidden" data-notify-product name="product" value="Birdeon launch list">
        <label class="sr-only" for="modal-email">Email address</label>
        <input id="modal-email" type="email" name="email" required autocomplete="email" placeholder="Email address">
        <button class="btn btn-orange" type="submit">Notify me</button>
        <p class="form-success" role="status">Thank you. When the shop opens, this list will be the first to hear.</p>
      </form>
    </div>
  </div>
  <script src="{p}assets/js/main.js"></script>
</body>
</html>
"""


def product_card(prod: dict, p: str) -> str:
    stem, alt = prod["images"][0]
    href = f"{p}products/{prod['slug']}.html"
    square = " square" if stem.startswith("forepack") or stem.startswith("summer-forepack") or stem.startswith("winter-forepack") or stem == "caps-v2" else ""
    return f"""
    <article class="card">
      <a href="{href}">
        <div class="card-media{square}">
          {picture(stem, alt, p)}
          <span class="badge">Coming soon</span>
        </div>
      </a>
      <div class="card-body">
        <h3><a href="{href}">{escape(prod['name'])}</a></h3>
        <p>{escape(prod['short'])}</p>
        <div class="card-actions">
          <a class="btn btn-outline btn-sm" href="{href}">View</a>
          <button class="btn btn-navy btn-sm" type="button" data-open-notify="{escape(prod['name'])}">Notify me</button>
        </div>
      </div>
    </article>"""


def paras(text: str) -> str:
    return "".join(f"<p>{escape(part.strip())}</p>" for part in text.split("\n\n") if part.strip())


def write(path: Path, content: str):
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content, encoding="utf-8")
    print("wrote", path.relative_to(ROOT), "chars", len(content))


def build_home():
    depth = 0
    p = prefix(depth)
    ld = {
        "@type": "WebSite",
        "@id": f"{SITE}/#website",
        "url": SITE,
        "name": "Birdeon",
        "description": "Birdeon golf apparel. Highland Hole Out, Winter League and Summer Links catalogues. Products coming soon.",
        "publisher": {"@id": f"{SITE}/#organization"},
        "inLanguage": "en",
    }
    html = head(
        title="Birdeon | Golf Apparel Coming Soon",
        description="Birdeon is a golf apparel brand with three catalogues — Highland Hole Out tartan, Winter League layers and Summer Links coral and aqua. Men's and women's golf polos, shorts, trousers, skirts, caps and a golf bag, coming soon in Australia, the Philippines and Taiwan.",
        canonical=f"{SITE}/",
        depth=0,
        extra_ld=ld,
        og_image=f"{SITE}/assets/images/og-default.jpg",
    )
    html += header(0, "home")
    html += f"""
  <main id="main">
    <section class="hero">
      <div class="hero-media">
        {picture("edd-swing-creme-leather", "Man swinging a golf club in a Birdeon navy tartan polo, cream shorts and cream cap on a palm-lined course", p, lazy=False)}
      </div>
      <div class="wrap hero-content">
        <p class="eyebrow">Golf apparel, coming soon</p>
        <h1>Colour on the course.</h1>
        <p class="lead">Birdeon is a new golf apparel label with three catalogues — tartan, winter layers and bright plain colour — for golfers in Australia, the Philippines and Taiwan.</p>
        <div class="hero-actions">
          <a class="btn btn-orange" href="#catalogues">Explore the catalogues</a>
          <button class="btn btn-ghost" type="button" data-open-notify>Notify me</button>
        </div>
      </div>
    </section>

    <section class="section" id="story">
      <div class="wrap story">
        <div class="story-images">
          {picture("herrera-reverse-navy", "Woman lining up a putt in the Birdeon women's navy tartan polo and reverse-colour tartan golf skirt", p, class_name="tall")}
          {picture("edd-beach-navy-leather", "Man by the water in the Birdeon men's navy tartan golf polo and navy shorts", p, class_name="wide")}
          <picture class="wide">
            <source type="image/webp" srcset="{p}assets/images/leather-tag-detail.webp">
            <img src="{p}assets/images/leather-tag-detail.jpg" width="1024" height="1024" alt="Close-up of a brown leather Birdeon chest tag stitched onto a navy, purple and orange tartan golf polo" loading="lazy" decoding="async">
          </picture>
        </div>
        <div>
          <p class="kicker">The brand</p>
          <h2>Tartan, colour, and a bird on the tag.</h2>
          <p>Birdeon is the golf apparel project of Damien Mueller and Edd Adair. The first three catalogues will be released individually: Highland Hole Out, the tartan set; Winter League, a darker collection with men's golf trousers; and Summer Links, bright coral and aqua in plain colour.</p>
          <p>Pieces are designed as looks — a polo, a short or skirt, a cap and socks — with a small leather chest tag on the shirts and a printed full-colour logo on the golf bag. Nothing is for sale yet. Fabric details are still to come, and every product on this site is marked coming soon.</p>
          <p><a class="btn btn-navy" href="{p}about.html">About Birdeon</a></p>
        </div>
      </div>
    </section>

    <section class="section" id="catalogues" style="padding-top:0">
      <div class="wrap">
        <div class="section-head">
          <p class="kicker">Three catalogues</p>
          <h2>Released individually, under one brand.</h2>
          <p class="muted">Browse the looks now. Products will be available soon.</p>
        </div>
        <div class="cat-grid">
"""
    for slug, cat in CATALOGUES.items():
        html += f"""
          <a class="cat-tile" href="{p}catalogues/{slug}.html">
            {picture(cat["tile"], cat["tile_alt"], p)}
            <div class="cat-tile-body">
              <p class="eyebrow">{escape(cat["eyebrow"])}</p>
              <h3>{escape(cat["name"])}</h3>
              <p>{escape(cat["tagline"])}</p>
            </div>
          </a>"""
    html += f"""
        </div>
      </div>
    </section>

    <section class="band" id="notify">
      <div class="wrap">
        <h2>Be first when the shop opens.</h2>
        <p class="lead">Birdeon products are not available yet. Leave your email and we will let you know when the catalogues go on sale.</p>
        <!-- Visual only: this form has no backend and does not store or send email addresses. -->
        <form class="notify-form inline" data-visual-form action="#" method="post">
          <label class="sr-only" for="home-email">Email address</label>
          <input id="home-email" type="email" name="email" required autocomplete="email" placeholder="Email address">
          <button class="btn btn-orange" type="submit">Notify me</button>
        </form>
        <p class="form-success" role="status">Thank you. When the shop opens, this list will be the first to hear.</p>
        <p class="form-note">This preview form does not send or store your address yet.</p>
      </div>
    </section>
  </main>
"""
    html += footer(0)
    write(ROOT / "index.html", html)


def build_about():
    p = prefix(0)
    html = head(
        title="About Birdeon | Golf Apparel by Damien Mueller and Edd Adair",
        description="Birdeon is a golf apparel brand from Damien Mueller and Edd Adair. Three catalogues — Highland Hole Out, Winter League and Summer Links — are on the way for golfers in Australia, the Philippines and Taiwan.",
        canonical=f"{SITE}/about.html",
        depth=0,
        extra_ld={"@type": "AboutPage", "name": "About Birdeon", "url": f"{SITE}/about.html", "isPartOf": {"@id": f"{SITE}/#website"}, "about": {"@id": f"{SITE}/#organization"}},
    )
    html += header(0, "about")
    html += f"""
  <main id="main">
    <header class="page-hero">
      <div class="wrap">
        <p class="kicker">About</p>
        <h1>A new name on the bag.</h1>
        <p class="lead">Birdeon is a golf apparel brand started by Damien Mueller and Edd Adair. The work so far is visual — catalogues of men's and women's golf clothing, still on their way to the shop floor.</p>
      </div>
    </header>
    <section class="section">
      <div class="wrap split-copy">
        <div>
          <h2>Who is behind Birdeon?</h2>
          <p>Damien Mueller, based in Australia, and Edd Adair lead the project together. The brand name is Birdeon. The first pieces are being designed as three catalogues, to be released individually rather than as a single drop.</p>
          <h2>What is coming?</h2>
          <p><strong>Highland Hole Out</strong> is the tartan collection: men's golf polos and shorts, women's polos with reverse-colour tartan golf skirts, leather-patch caps, and a navy tartan golf bag with the printed full-colour logo.</p>
          <p><strong>Winter League</strong> goes darker, with men's charcoal golf trousers and a forest quarter-zip, plus a women's burgundy and forest tartan set that keeps a skirt.</p>
          <p><strong>Summer Links</strong> is bright and plain — coral and aqua, without tartan — for warm-weather golf.</p>
          <p>The clothes are being designed with golfers in Australia, the Philippines and Taiwan in mind. Fabric details, sizes and prices will follow. Nothing on this site is for sale yet.</p>
          <p><a class="btn btn-navy" href="contact.html">Get in touch</a></p>
        </div>
        <div class="about-photos">
          {picture("edd-swing-creme-leather", "Birdeon men's navy tartan polo worn with cream golf shorts on a palm-lined course", p, class_name="span2")}
          {picture("herrera-reverse-pink-lemon", "Birdeon women's pink and lemon tartan golf polo and reverse tartan skirt", p)}
          <picture>
            <source type="image/webp" srcset="{p}assets/images/leather-tag-detail.webp">
            <img src="{p}assets/images/leather-tag-detail.jpg" width="1024" height="1024" alt="Leather Birdeon chest tag on a navy tartan golf polo" loading="lazy" decoding="async">
          </picture>
        </div>
      </div>
    </section>
  </main>
"""
    html += footer(0)
    write(ROOT / "about.html", html)


def build_contact():
    html = head(
        title="Contact Birdeon | Notify Me When Golf Apparel Arrives",
        description="Get in touch with Birdeon or leave your email to be notified when Highland Hole Out, Winter League and Summer Links golf apparel becomes available.",
        canonical=f"{SITE}/contact.html",
        depth=0,
        extra_ld={"@type": "ContactPage", "name": "Contact Birdeon", "url": f"{SITE}/contact.html"},
    )
    html += header(0, "contact")
    html += """
  <main id="main">
    <header class="page-hero">
      <div class="wrap">
        <p class="kicker">Contact</p>
        <h1>Say hello, or ask to be notified.</h1>
        <p class="lead">This is a visual preview. The form below does not send a message yet — it is here to show how contact will work when the shop opens.</p>
      </div>
    </header>
    <section class="section">
      <div class="wrap contact-grid">
        <div>
          <h2>Before the shop opens</h2>
          <p>Birdeon is not taking orders, and we have not published a public inbox on this preview. When the catalogues become available, this page will be the place to reach the team.</p>
          <p>If you want to hear when products are available, use the notify form. If you have a question about the brand or the catalogues, use the message form — both are visual only for now.</p>
          <p class="muted">Australia · Philippines · Taiwan</p>
        </div>
        <div>
          <h2>Message Birdeon</h2>
          <!-- Visual only: this contact form has no backend and does not store or send messages. -->
          <form class="contact-form" data-visual-form action="#" method="post">
            <div class="field">
              <label for="c-name">Name</label>
              <input id="c-name" name="name" type="text" required autocomplete="name">
            </div>
            <div class="field">
              <label for="c-email">Email</label>
              <input id="c-email" name="email" type="email" required autocomplete="email">
            </div>
            <div class="field">
              <label for="c-msg">Message</label>
              <textarea id="c-msg" name="message" rows="6" required></textarea>
            </div>
            <button class="btn btn-navy" type="submit">Send message</button>
            <p class="form-success" role="status">Thank you. When contact is connected, messages like this will reach the Birdeon team.</p>
            <p class="form-note">This preview form does not send or store your message yet.</p>
          </form>
        </div>
      </div>
    </section>
  </main>
"""
    html += footer(0)
    write(ROOT / "contact.html", html)


def build_catalogue(slug: str):
    cat = CATALOGUES[slug]
    products = by_catalogue(slug)
    p = prefix(1)
    item_list = {
        "@type": "CollectionPage",
        "name": cat["name"],
        "url": f"{SITE}/catalogues/{slug}.html",
        "description": cat["description"],
        "isPartOf": {"@id": f"{SITE}/#website"},
        "mainEntity": {
            "@type": "ItemList",
            "itemListElement": [
                {
                    "@type": "ListItem",
                    "position": i + 1,
                    "url": f"{SITE}/products/{prod['slug']}.html",
                    "name": prod["name"],
                }
                for i, prod in enumerate(products)
            ],
        },
    }
    html = head(
        title=cat["title"],
        description=cat["description"],
        canonical=f"{SITE}/catalogues/{slug}.html",
        depth=1,
        og_image=f"{SITE}/assets/images/products/{cat['hero']}.jpg",
        og_alt=cat["tile_alt"],
        extra_ld=item_list,
    )
    html += header(1, slug)
    html += f"""
  <main id="main">
    <header class="page-hero with-image">
      <div class="page-hero-bg">
        {picture(cat["hero"], cat["tile_alt"], p, lazy=False)}
      </div>
      <div class="wrap">
        <p class="kicker">{escape(cat["eyebrow"])}</p>
        <h1>{escape(cat["name"])}</h1>
        <p class="lead">{escape(cat["intro"])}</p>
      </div>
    </header>
    <section class="section">
      <div class="wrap">
        <div class="toolbar">
          <div>
            <h2>The {escape(cat["name"])} pieces</h2>
            <p class="muted">{len(products)} products · every piece coming soon</p>
          </div>
        </div>
        <div class="product-grid">
          {"".join(product_card(prod, p) for prod in products)}
        </div>
      </div>
    </section>
  </main>
"""
    html += footer(1)
    write(ROOT / "catalogues" / f"{slug}.html", html)


def build_product(prod: dict):
    p = prefix(1)
    cat = CATALOGUES[prod["catalogue"]]
    url = f"{SITE}/products/{prod['slug']}.html"
    first_stem, first_alt = prod["images"][0]
    og = f"{SITE}/assets/images/products/{first_stem}.jpg"
    paragraphs = [s.strip() for s in prod["description"].split("\n\n") if s.strip()]
    product_ld = {
        "@type": "Product",
        "name": prod["name"],
        "description": " ".join(paragraphs),
        "image": [f"{SITE}/assets/images/products/{s}.jpg" for s, _ in prod["images"]],
        "brand": {"@type": "Brand", "name": "Birdeon"},
        "sku": prod["slug"],
        "category": prod["kind"],
        "url": url,
        "isPartOf": {"@id": f"{SITE}/#organization"},
        "offers": {
            "@type": "Offer",
            "url": url,
            "availability": "https://schema.org/PreOrder",
            "itemCondition": "https://schema.org/NewCondition",
            "eligibleRegion": [
                {"@type": "Country", "name": "Australia"},
                {"@type": "Country", "name": "Philippines"},
                {"@type": "Country", "name": "Taiwan"},
            ],
        },
    }
    crumbs = {
        "@type": "BreadcrumbList",
        "itemListElement": [
            {"@type": "ListItem", "position": 1, "name": "Home", "item": f"{SITE}/"},
            {"@type": "ListItem", "position": 2, "name": cat["name"], "item": f"{SITE}/catalogues/{prod['catalogue']}.html"},
            {"@type": "ListItem", "position": 3, "name": prod["name"], "item": url},
        ],
    }
    meta_desc = paragraphs[0]
    if len(meta_desc) > 160:
        # trim on a word
        cut = meta_desc[:157].rsplit(" ", 1)[0] + "…"
        meta_desc = cut
    html = head(
        title=f"{prod['name']} | {cat['name']} | Birdeon",
        description=meta_desc,
        canonical=url,
        depth=1,
        og_type="product",
        og_image=og,
        og_alt=first_alt,
        extra_ld=[product_ld, crumbs],
    )
    html += header(1, prod["catalogue"])
    thumbs = ""
    for i, (stem, alt) in enumerate(prod["images"]):
        w, h = img_size(stem)
        src = f"{p}assets/images/products/{stem}.jpg"
        webp = f"{p}assets/images/products/{stem}.webp"
        active = " is-active" if i == 0 else ""
        thumbs += f"""
          <button type="button" class="{'is-active' if i==0 else ''}" data-thumb data-src="{src}" data-webp="{webp}" data-alt="{escape(alt)}" aria-label="Show image {i+1}">
            <img src="{src}" width="{w}" height="{h}" alt="" loading="lazy">
          </button>"""
    html += f"""
  <main id="main">
    <div class="wrap">
      <nav class="crumb" aria-label="Breadcrumb">
        <a href="{p}index.html">Home</a> ·
        <a href="{p}catalogues/{prod['catalogue']}.html">{escape(cat['name'])}</a> ·
        <span>{escape(prod['name'])}</span>
      </nav>
    </div>
    <article class="wrap product-layout">
      <div>
        <div class="gallery-main">
          <picture>
            <source type="image/webp" srcset="{p}assets/images/products/{first_stem}.webp" data-gallery-webp>
            <img src="{p}assets/images/products/{first_stem}.jpg" width="{img_size(first_stem)[0]}" height="{img_size(first_stem)[1]}" alt="{escape(first_alt)}" fetchpriority="high" decoding="async" data-gallery-main>
          </picture>
        </div>
        <div class="thumbs">{thumbs}
        </div>
      </div>
      <div class="product-info">
        <span class="badge">Coming soon</span>
        <p class="kicker">{escape(cat['name'])} · {escape(prod['kind'])}</p>
        <h1>{escape(prod['name'])}</h1>
        <div class="desc">{paras(prod['description'])}</div>
        <button class="btn btn-orange" type="button" data-open-notify="{escape(prod['name'])}">Notify me</button>
        <p class="fine-print">This piece is not for sale yet. There is no price, cart or checkout on this preview. Fabric details coming soon.</p>
      </div>
    </article>
"""
    rel = []
    for slug in prod.get("related", []):
        if slug in BY_SLUG:
            rel.append(BY_SLUG[slug])
    # fill with same catalogue if needed
    if len(rel) < 3:
        for other in by_catalogue(prod["catalogue"]):
            if other["slug"] != prod["slug"] and other not in rel:
                rel.append(other)
            if len(rel) >= 3:
                break
    rel = rel[:3]
    if rel:
        html += f"""
    <section class="related">
      <div class="wrap">
        <h2>You may also like</h2>
        <div class="product-grid">
          {"".join(product_card(r, p) for r in rel)}
        </div>
      </div>
    </section>
"""
    html += "  </main>\n"
    html += footer(1)
    write(ROOT / "products" / f"{prod['slug']}.html", html)


def build_robots():
    write(ROOT / "robots.txt", """User-agent: *
Allow: /
Disallow: /screenshots/
Disallow: /build.py

Sitemap: https://birdeon.com/sitemap.xml
""")


def build_sitemap():
    urls = [
        (f"{SITE}/", "1.0", "weekly"),
        (f"{SITE}/about.html", "0.7", "monthly"),
        (f"{SITE}/contact.html", "0.6", "monthly"),
    ]
    for slug in CATALOGUES:
        urls.append((f"{SITE}/catalogues/{slug}.html", "0.8", "weekly"))
    for prod in PRODUCTS:
        urls.append((f"{SITE}/products/{prod['slug']}.html", "0.7", "weekly"))
    lastmod = "2026-11-13"
    parts = ['<?xml version="1.0" encoding="UTF-8"?>', '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">']
    for loc, pri, freq in urls:
        parts.append(
            f"  <url><loc>{loc}</loc><lastmod>{lastmod}</lastmod><changefreq>{freq}</changefreq><priority>{pri}</priority></url>"
        )
    parts.append("</urlset>\n")
    write(ROOT / "sitemap.xml", "\n".join(parts))


def build_manifest():
    data = {
        "name": "Birdeon",
        "short_name": "Birdeon",
        "description": "Birdeon golf apparel. Coming soon.",
        "start_url": "/",
        "display": "browser",
        "background_color": "#000926",
        "theme_color": "#000926",
        "icons": [
            {"src": "assets/icons/icon-192.png", "sizes": "192x192", "type": "image/png"},
            {"src": "assets/icons/icon-512.png", "sizes": "512x512", "type": "image/png"},
        ],
    }
    write(ROOT / "site.webmanifest", json.dumps(data, indent=2))


def main():
    # Fix leather tag on home: use picture-like jpg+webp
    build_home()
    build_about()
    build_contact()
    for slug in CATALOGUES:
        build_catalogue(slug)
    for prod in PRODUCTS:
        build_product(prod)
    build_robots()
    build_sitemap()
    build_manifest()
    print("DONE", "pages", 3 + len(CATALOGUES) + len(PRODUCTS), "products", len(PRODUCTS))


if __name__ == "__main__":
    main()
