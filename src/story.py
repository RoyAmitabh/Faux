from utils import *


def build_story_context():
    return {
        "basic": generate_basic_data(),
        "business": generate_business_data(),
        "internet": generate_internet_data(),
        "profile": generate_profile_data(),
        "datetime": generate_date_time_data(),
        "misc": generate_misc_data(),
    }

def generate_story(context):
    b = context["basic"]
    bus = context["business"]
    net = context["internet"]
    prof = context["profile"]
    dt = context["datetime"]
    misc = context["misc"]

    paragraphs = []

    paragraphs.append(f"""
Meet {b['name']}, a {bus['job']} at {bus['company']}. Residing at {b['address'].replace(chr(10), ', ')}, {b['name']} enjoys a fast-paced career that often involves juggling complex projects while managing a team of top performers. Born on {prof['birthdate'].strftime('%B %d, %Y')}, they’ve always been passionate about technology and problem-solving.
    """)

    paragraphs.append(f"""
Outside of work, {b['name']} is an avid internet user. You might spot them online with the username @{net['user_name']} or sending emails from {b['email']}. When surfing the web, they often explore sites hosted on domains like {net['domain_name']}, connected via an IPv4 address such as {net['ipv4']} and a MAC address {net['mac_address']}.
    """)

    paragraphs.append(f"""
Their personal profile reveals even more — they identify as {prof['sex']} and currently reside in {prof['residence']}. Fluent in {misc['language']}, they enjoy the finer things in life, especially anything in {misc['color']} — their favorite color. They are also known for keeping their finances secure, armed with a credit card ending in {bus['credit_card'][-4:]}.
    """)

    paragraphs.append(f"""
Recently, {b['name']} scheduled an appointment on {dt['iso8601']}. Their unique client ID for this booking? {misc['uuid']}. When not in meetings, you’ll often find them sipping coffee, reviewing reports, and pondering the ever-changing value of the {misc['currency']}.
    """)

    return "\n".join(paragraphs)

# Generate and print story
context = build_story_context()
story = generate_story(context)
print(story)
