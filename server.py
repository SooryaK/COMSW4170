from flask import Flask
from flask import render_template
from flask import Response, request, jsonify
app = Flask(__name__)


current_id = 30
podcasts = [
    {
        "ID": "1",
        "Title": "Fantasy Footballers - Fantasy Football Podcast",
        "Image": "http://is3.mzstatic.com/image/thumb/Music118/v4/64/67/a4/6467a467-0263-9e8d-bd48-92c49f5df164/source/600x600bb.jpg",
        "Description": "Fantasy Football at it's very best.  Say goodbye to the talking heads of Fantasy Football and hello to The Fantasy Footballers.  The expert trio of Andy Holloway, Jason Moore, and Mike \"The Fantasy Hitman\" Wright break down the world of Fantasy Football with astute analysis, strong opinions, and matchup-winning advice you can't get anywhere else.  A high quality and entertaining show that will win you your Fantasy Football league -- in style.  The ONE Fantasy Football Podcast you can't leave off your roster.",
        "Language": "English",
        "Category": [
            {"Name":"Professional", "mark_as_deleted": False},
            {"Name":"Games & Hobbies", "mark_as_deleted": False},
            {"Name":"Sports & Recreation", "mark_as_deleted": False}
        ],
        "Website": "https://www.thefantasyfootballers.com",
        "Author": "The Fantasy Footballers",
        "Rating": "4.3",
    },
    {
        "ID": "2",
        "Title": "How I Built This with Guy Raz",
        "Image": "http://is2.mzstatic.com/image/thumb/Music118/v4/f1/68/f7/f168f737-eb33-2880-a37c-32146e27d306/source/600x600bb.jpg",
        "Description": "Host Guy Raz dives into the stories behind some of the world's best known companies. How I Built This weaves a narrative journey about innovators, entrepreneurs, idealists, and the movements they built.",
        "Language": "English",
        "Category": [
            {"Name":"Business", "mark_as_deleted": False}
        ],
        "Website": "http://www.npr.org/series/490248027/how-i-built-this",
        "Author": "NPR",
        "Rating": "4.6"
    },
    {
        "ID": "3",
        "Title": "Motley Fool Answers",
        "Image": "http://is4.mzstatic.com/image/thumb/Music118/v4/5f/1c/10/5f1c1049-099b-952a-e4fb-c429cdc2a705/source/600x600bb.jpg",
        "Description": "Saving, spending, planning you've got money questions and we've got answers. Every week host Alison Southwick and personal finance expert Robert Brokamp challenge the conventional wisdom on life's biggest financial issues to reveal what you really need to know to make smart money moves. Send your questions to answers@fool.com.",
        "Language": "English",
        "Category": [
            {"Name":"Education", "mark_as_deleted": False},
            {"Name":"Investing", "mark_as_deleted": False},
            {"Name":"Business", "mark_as_deleted": False}
        ],
        "Website": "http://www.fool.com/podcasts/answers",
        "Author": "The Motley Fool",
        "Rating": "4.5"
    },
    {
        "ID": "4",
        "Title": "The Bill Simmons Podcast",
        "Image": "http://is1.mzstatic.com/image/thumb/Music118/v4/84/46/0b/84460bae-caa2-7f39-4d33-b6376ee88a14/source/600x600bb.jpg",
        "Description": "HBO and The Ringer's Bill Simmons hosts the most downloaded sports podcast of all time, with a rotating crew of celebrities, athletes, and media staples, as well as mainstays like Cousin Sal, Joe House, and a slew of other friends and family members who always happen to be suspiciously available.",
        "Language": "English",
        "Category": [
            {"Name":"Professional", "mark_as_deleted": False},
            {"Name":"Sports & Recreation", "mark_as_deleted": False}
        ],
        "Website": "https://art19.com/shows/the-bill-simmons-podcast",
        "Author": "The Ringer",
        "Rating": "4.5"
    },
    {
        "ID": "5",
        "Title": "Planet Money",
        "Image": "http://is3.mzstatic.com/image/thumb/Music62/v4/9c/26/62/9c266213-2a31-e6bd-ced0-3f88bffa52c7/source/600x600bb.jpg",
        "Description": "The economy, explained, with stories and surprises. Imagine you could call up a friend and say, \"Meet me at the bar and tell me what's going on with the economy.\" Now imagine that's actually a fun evening. That's what we're going for at <em>Planet Money</em>. People seem to like it.",
        "Language": "English",
        "Category": [
            {"Name":"Business", "mark_as_deleted": False},
            {"Name":"News & Politics", "mark_as_deleted": False}
        ],
        "Website": "http://www.npr.org/planetmoney",
        "Author": "NPR",
        "Rating": "4.2"
    },
    {
        "ID": "6",
        "Title": "Stuff You Should Know",
        "Image": "http://is1.mzstatic.com/image/thumb/Music128/v4/ce/3f/27/ce3f27a5-b96d-f87e-6025-bd4b9eaa027f/source/600x600bb.jpg",
        "Description": "How do landfills work? How do mosquitos work? Join Josh and Chuck as they explore the Stuff You Should Know about everything from genes to the Galapagos in this podcast from HowStuffWorks.com.",
        "Language": "English",
        "Category": [
            {"Name":"Society & Culture", "mark_as_deleted": False}
        ],
        "Website": "https://www.howstuffworks.com/",
        "Author": "HowStuffWorks",
        "Rating": "4.7"
    },
    {
        "ID": "7",
        "Title": "Pardon My Take",
        "Image": "http://is5.mzstatic.com/image/thumb/Music62/v4/b7/e4/67/b7e46778-c171-9c44-ba31-cf42705467c7/source/600x600bb.jpg",
        "Description": "On \"Pardon My Take,\" Big Cat & PFT Commenter deliver the loudest and most correct sports takes in the history of the spoken word. Daily topics, guests, and an inability to tell what the hosts might be doing will make this your new favorite sports talk show. This is a podcast that will without a doubt change your life for the better- guaranteed, or your money back. *Pretend a reggaeton air horn is going off right now*",
        "Language": "English",
        "Category": [
            {"Name":"Comedy", "mark_as_deleted": False},
            {"Name":"Sports & Recreation", "mark_as_deleted": False},
            {"Name":"Society & Culture", "mark_as_deleted": False}
        ],
        "Website": "http://www.barstoolsports.com",
        "Author": "Barstool Engineering",
        "Rating": "4.7"
    },
    {
        "ID": "8",
        "Title": "Invisibilia",
        "Image": "http://is5.mzstatic.com/image/thumb/Music62/v4/f9/5a/c6/f95ac62d-accd-4228-d8f2-f5559f31bb69/source/600x600bb.jpg",
        "Description": "Unseeable forces control human behavior and shape our ideas, beliefs, and assumptions. Invisibilia is Latin for invisible things fuses narrative storytelling with science that will make you see your own life differently.",
        "Language": "English",
        "Category": [
            {"Name":"Science & Medicine", "mark_as_deleted": False},
            {"Name":"Society & Culture", "mark_as_deleted": False}
        ],
        "Website": "http://www.npr.org/programs/invisibilia",
        "Author": "NPR",
        "Rating": "4.8"
    },
    {
        "ID": "9",
        "Title": "Modern Love",
        "Image": "http://is4.mzstatic.com/image/thumb/Music71/v4/8f/5d/68/8f5d68de-6ef6-98e8-8f84-91abc2e3cfc4/source/600x600bb.jpg",
        "Description": "Stories of love, loss and redemption.",
        "Language": "English",
        "Category": [
            {"Name":"Society & Culture", "mark_as_deleted": False}
        ],
        "Website": "http://wbur.org/modernlove",
        "Author": "WBUR and The New York Times",
        "Rating": "4.6"
    },
    {
        "ID": "10",
        "Title": "Binge Mode: Weekly",
        "Image": "http://is5.mzstatic.com/image/thumb/Music118/v4/2c/6a/69/2c6a69d8-c29c-875f-7ec6-c68ee42d9c91/source/600x600bb.jpg",
        "Description": "Join The Ringer's Mallory Rubin and Jason Concepcion on their signature deep dives into the topics obsessing them at the moment, from shows and movies to books and sports.",
        "Language": "English",
        "Category": [
            {"Name":"TV & Film", "mark_as_deleted": False}
        ],
        "Website": "https://art19.com/shows/binge-mode-game-of-thrones",
        "Author": "The Ringer",
        "Rating": "4.2"
    },
    {
        "ID": "11",
        "Title": "Recode Decode, hosted by Kara Swisher",
        "Image": "http://is5.mzstatic.com/image/thumb/Music62/v4/8c/43/83/8c4383ee-a7cd-6fcb-49df-6245c46fdd10/source/600x600bb.jpg",
        "Description": "One of tech's most prominent journalists, Kara Swisher is known for her insightful reporting and straight-shooting style. Listen in as she hosts hard-hitting interviews about the week in tech with influential business leaders and outspoken personalities from media, politics and more.",
        "Language": "English",
        "Category": [
            {"Name":"Gadgets", "mark_as_deleted": False},
            {"Name":"Technology", "mark_as_deleted": False},
            {"Name":"Tech News", "mark_as_deleted": False}
        ],
        "Website": "http://recode.net/podcast/recode-decode-hosted-by-kara-swisher/",
        "Author": "Recode",
        "Rating": "4.6"
    },
    {
        "ID": "12",
        "Title": "Pod Save America",
        "Image": "http://is4.mzstatic.com/image/thumb/Music122/v4/c9/68/50/c96850f5-ed6e-fe5e-59d1-fe5be5c54606/source/600x600bb.jpg",
        "Description": "Four former aides to President Obama, Jon Favreau, Dan Pfeiffer, Jon Lovett, and Tommy Vietor, are joined by journalists, politicians, comedians, and activists for a freewheeling conversation about politics, the press and the challenges posed by the Trump presidency.",
        "Language": "English",
        "Category": [
            {"Name":"News & Politics", "mark_as_deleted": False}
        ],
        "Website": "https://art19.com/shows/pod-save-america",
        "Author": "Crooked Media",
        "Rating": "4.7"
    },
    {
        "ID": "13",
        "Title": "TED Radio Hour",
        "Image": "http://is3.mzstatic.com/image/thumb/Music71/v4/21/3a/3e/213a3e55-3264-653c-7fda-b8ef4dc39bbf/source/600x600bb.jpg",
        "Description": "The TED Radio Hour is a journey through fascinating ideas, astonishing inventions, fresh approaches to old problems, and new ways to think and create.",
        "Language": "English",
        "Category": [
            {"Name":"Arts", "mark_as_deleted": False},
            {"Name":"Society & Culture", "mark_as_deleted": False},
            {"Name":"Technology", "mark_as_deleted": False}
        ],
        "Website": "http://www.npr.org/programs/ted-radio-hour/",
        "Author": "NPR",
        "Rating": "4.1"
    },
    {
        "ID": "14",
        "Title": "Crimetown",
        "Image": "http://is4.mzstatic.com/image/thumb/Music71/v4/f1/31/3a/f1313a60-f63f-3be9-31aa-5fbd5832a196/source/600x600bb.jpg",
        "Description": "Welcome to Crimetown, a new series from Gimlet Media and the creators of HBO's The Jinx. Every season, we'll investigate the culture of crime in a different American city. First up: Providence, Rhode Island, where organized crime and corruption infected every aspect of public life. This is a story of alliances and betrayals, of heists and stings, of crooked cops and honest mobsters a story where it's hard to tell the good guys from the bad guys. Hosted by Marc Smerling and Zac Stuart-Pontier.",
        "Language": "English",
        "Category": [
            {"Name":"News & Politics", "mark_as_deleted": False}
        ],
        "Website": "https://www.gimletmedia.com/show/crimetown",
        "Author": "Gimlet",
        "Rating": "4.3"
    },
    {
        "ID": "15",
        "Title": "StartUp Podcast",
        "Image": "http://is1.mzstatic.com/image/thumb/Music118/v4/93/98/08/93980897-bc63-ec24-a523-cbb6a6e9670a/source/600x600bb.jpg",
        "Description": "A series about what it's really like to start a business.",
        "Language": "English",
        "Category": [
            {"Name":"Careers", "mark_as_deleted": False}, 
            {"Name":"Business", "mark_as_deleted": False}
        ],
        "Website": "http://gimletmedia.com",
        "Author": "Gimlet",
        "Rating": "4.8"
    },
    {
        "ID": "16",
        "Title": "Reply All",
        "Image": "http://is2.mzstatic.com/image/thumb/Music111/v4/6c/9e/5f/6c9e5f7e-aed2-b477-516d-af319c09aa49/source/600x600bb.jpg",
        "Description": "\"'A podcast about the internet' that is actually an unfailingly original exploration of modern life and how to survive it.\" - The Guardian. Hosted by PJ Vogt and Alex Goldman, from Gimlet.",
        "Language": "English",
        "Category": [
            {"Name":"Technology", "mark_as_deleted": False}
        ],
        "Website": "http://gimletmedia.com/shows/reply-all",
        "Author": "Gimlet",
        "Rating": "4.7"
    },
    {
        "ID": "17",
        "Title": "Why'd You Push That Button?",
        "Image": "http://is5.mzstatic.com/image/thumb/Music118/v4/2a/55/39/2a553953-bec2-5c53-4d14-50f175f88b2d/source/600x600bb.jpg",
        "Description": "The Verge's Ashley Carman and Kaitlyn Tiffany ask the hard, weird, and occasionally dumb questions about how your tiny tech decisions impact your social life. Do you turn read receipts on? Do you share your Netflix passwords with friends? Why'd You Push That Button examines the choices technology forces us to make, through interviews with consumers, developers, friends, and strangers.",
        "Language": "English",
        "Category": [
            {"Name":"Technology", "mark_as_deleted": False},
            {"Name":"Society & Culture", "mark_as_deleted": False}
        ],
        "Website": "https://art19.com/shows/whyd-you-push-that-button",
        "Author": "Vox Media",
        "Rating": "4.6"
    },
    {
        "ID": "18",
        "Title": "The Impact",
        "Image": "http://is4.mzstatic.com/image/thumb/Music118/v4/59/94/8f/59948fff-139d-5dff-2e1f-03fa42fc11f5/source/600x600bb.jpg",
        "Description": " In Washington, the story often ends when Congress passes a law. For The Impact, thats where our story begins. We focus on the human consequences of policy-making, what happens in the real world after the government, non-profits, even academic institutions start doing something differently. The Impact looks at policies that work and policies that need some work as they make their way out into the real world, with many surprises along the way.",
        "Language": "English",
        "Category": [
            {"Name":"News & Politics", "mark_as_deleted": False}
        ],
        "Website": "https://art19.com/shows/the-impact",
        "Author": "Vox Media",
        "Rating": "4.3"
    },
    {
        "ID": "19",
        "Title": "The Ringer NBA Show",
        "Image": "http://is3.mzstatic.com/image/thumb/Music128/v4/a5/cb/e0/a5cbe0ba-5fe1-b618-007c-e84ff4f92932/source/600x600bb.jpg",
        "Description": "A daily breakdown of the latest story lines, trends, and important developments in the NBA. We promise to keep the Sixers and Celtics discussion to a reasonable amount or to at least try.",
        "Language": "English",
        "Category": [
            {"Name":"Sports & Recreation", "mark_as_deleted": False},
            {"Name":"Professional", "mark_as_deleted": False}
        ],
        "Website": "https://art19.com/shows/the-ringer-nba-show",
        "Author": "The Ringer",
        "Rating": "4.4"
    },
    {
        "ID": "20",
        "Title": "The Ringer NFL Show",
        "Image": "http://is1.mzstatic.com/image/thumb/Music128/v4/4f/a1/f6/4fa1f613-2520-21dc-7314-4863545c8870/source/600x600bb.jpg",
        "Description": "The Ringer NFL Show features a rotating group of Ringer NFL experts, including Michael Lombardi, Robert Mays, Kevin Clark, and Danny Kelly. The show will also feature ex-players and coaches, among others, as guests.",
        "Language": "English",
        "Category": [
            {"Name":"Sports & Recreation", "mark_as_deleted": False},
            {"Name":"Professional", "mark_as_deleted": False}
        ],
        "Website": "https://art19.com/shows/the-ringer-nfl-show",
        "Author": "The Ringer",
        "Rating": "4.6"
    },
    {
        "ID": "21",
        "Title": "The Rewatchables",
        "Image": "http://is5.mzstatic.com/image/thumb/Music118/v4/20/5d/f3/205df39c-5bd4-35ff-e917-8da280e77585/source/600x600bb.jpg",
        "Description": " 'The Rewatchables,' the newest film podcast from the Ringer Podcast Network, features HBO and The Ringer's Bill Simmons and a roundtable of people from The Ringer universe discussing movies they can't seem to stop watching.",
        "Language": "English",
        "Category": [
            {"Name":"TV & Film", "mark_as_deleted": False}
        ],
        "Website": "https://art19.com/shows/the-rewatchables",
        "Author": "The Ringer",
        "Rating": "4.7"
    },
    {
        "ID": "22",
        "Title": "Tiny Desk Concerts - Audio",
        "Image": "http://is2.mzstatic.com/image/thumb/Music62/v4/67/5e/ea/675eeadb-d627-6dbb-d2b8-e2482ab5e50e/source/600x600bb.jpg",
        "Description": "Tiny Desk Concerts from NPR Music feature your favorite musicians performing at All Songs Considered host Bob Boilen's desk in the NPR office. Hear Wilco, Adele, Passion Pit, Tinariwen, Miguel, The xx and many more. This is the audio version of the podcast. A video version is also available.",
        "Language": "English",
        "Category": [
            {"Name":"Music", "mark_as_deleted": False}
        ],
        "Website": "http://www.npr.org/tinydeskconcerts",
        "Author": "NPR",
        "Rating": "4.5"
    },
    {
        "ID": "23",
        "Title": "Car Talk",
        "Image": "http://is4.mzstatic.com/image/thumb/Music62/v4/1c/38/70/1c387072-f4fc-19f0-4000-f1295e282654/source/600x600bb.jpg",
        "Description": "America's funniest auto mechanics take calls from weary car owners all over the country, and crack wise while they diagnose Dodges and dismiss Diahatsus. You don't have to know anything about cars to love this one hour weekly laugh fest.",
        "Language": "English",
        "Category": [
            {"Name":"Automotive", "mark_as_deleted": False},
            {"Name":"Games & Hobbies", "mark_as_deleted": False},
            {"Name":"Comedy", "mark_as_deleted": False}
        ],
        "Website": "http://www.cartalk.com",
        "Author": "NPR",
        "Rating": "4.6"
    },
    {
        "ID": "24",
        "Title": "The Bill Barnwell Show",
        "Image": "http://is1.mzstatic.com/image/thumb/Music117/v4/01/de/ee/01deee31-de1c-f774-9ff1-a58a7dd8f7c2/source/600x600bb.jpg",
        "Description": "Bill Barnwell and friends talk all things sports and beyond.",
        "Language": "English",
        "Category": [
            {"Name":"Sports & Recreation", "mark_as_deleted": False}
        ],
        "Website": "http://www.espn.com/espnradio/podcast/index",
        "Author": "ESPN",
        "Rating": "4.4"
    },
    {
        "ID": "25",
        "Title": "The Dave Ramsey Show",
        "Image": "http://is3.mzstatic.com/image/thumb/Music122/v4/bf/66/2a/bf662a19-407b-bf4a-9ffe-1478109ec225/source/600x600bb.jpg",
        "Description": "The Dave Ramsey Show is about real life and how it revolves around money. Dave Ramsey teaches you to manage and budget your money, get out of debt, build wealth, and live in financial peace. Managing your money properly will reduce stress, improve your marriage, and provide security for you and your family. Updated: Tue, 18 Aug 2015",
        "Language": "English",
        "Category": [
            {"Name":"Business", "mark_as_deleted": False},
            {"Name":"Investing", "mark_as_deleted": False}
        ],
        "Website": "http://www.daveramsey.com?ectid=itunes",
        "Author": "Lampo Licensing, LLC.",
        "Rating": "4.7"
    },
    {
        "ID": "26",
        "Title": "Fresh Air",
        "Image": "http://is2.mzstatic.com/image/thumb/Music118/v4/6c/b6/ab/6cb6ab65-91d0-5a25-5199-9bae5bf2e89b/source/600x600bb.jpg",
        "Description": "Fresh Air from WHYY, the Peabody Award-winning weekday magazine of contemporary arts and issues, is one of public radio's most popular programs. Hosted by Terry Gross, the show features intimate conversations with today's biggest luminaries.",
        "Language": "English",
        "Category": [
            {"Name":"Society & Culture", "mark_as_deleted": False},
            {"Name":"TV & Film", "mark_as_deleted": False},
            {"Name":"Arts", "mark_as_deleted": False}
        ],
        "Website": "http://www.npr.org/programs/fresh-air/",
        "Author": "NPR",
        "Rating": "4.3"
    },
    {
        "ID": "27",
        "Title": "Radiolab",
        "Image": "http://is1.mzstatic.com/image/thumb/Music127/v4/e2/e0/ea/e2e0ead8-a98b-788d-c384-cc4cdc01aaaf/source/600x600bb.jpg",
        "Description": "A two-time Peabody Award-winner, Radiolab is an investigation told through sounds and stories, and centered around one big idea. In the Radiolab world, information sounds like music and science and culture collide. Hosted by Jad Abumrad and Robert Krulwich, the show is designed for listeners who demand skepticism, but appreciate wonder. \n\nWNYC Studios is the producer of other leading podcasts including Freakonomics Radio, Death, Sex & Money, On the Media and many more.",
        "Language": "English",
        "Category": [
            {"Name":"Society & Culture", "mark_as_deleted": False},
            {"Name":"Education", "mark_as_deleted": False},
            {"Name":"Science & Medicine", "mark_as_deleted": False},
            {"Name":"Natural Sciences", "mark_as_deleted": False}
        ],
        "Website": "http://www.radiolab.org/series/podcasts/",
        "Author": "WNYC Studios",
        "Rating": "4.2"
    },
    {
        "ID": "28",
        "Title": "2 Dope Queens",
        "Image": "http://is4.mzstatic.com/image/thumb/Music117/v4/39/02/9b/39029b19-edba-f441-0c8d-0fbb9da75896/source/600x600bb.jpg",
        "Description": "Phoebe Robinson and Jessica Williams are funny. They're black. They're BFFs. And they host a live comedy show in Brooklyn. Join the 2 Dope Queens, along with their favorite comedians, for stories about sex, romance, race, hair journeys, living in New York, and Billy Joel. Plus a whole bunch of other s**t. WNYC Studios is the producer of other leading podcasts including Radiolab, Death, Sex & Money, Freakonomics Radio, Note to  Self and many more.",
        "Language": "English",
        "Category": [
            {"Name":"Comedy", "mark_as_deleted": False}
        ],
        "Website": "http://www.wnyc.org/shows/dopequeens",
        "Author": "WNYC Studios",
        "Rating": "4.7"
    },
    {
        "ID": "29",
        "Title": "The Pitch",
        "Image": "http://is3.mzstatic.com/image/thumb/Music111/v4/b9/00/04/b90004b9-539c-8911-e206-bc5b23f87e9f/source/600x600bb.jpg",
        "Description": "Real entrepreneurs pitch to real investors for real money. In each episode, we take you behind closed doors to the critical moment when aspiring entrepreneurs put it all on the line. The Pitch delivers on the high-stakes promise of a live pitch without shying away from the nitty gritty details of what happens after everyone shakes hands and walks out of the room. Hosted by Josh Muccio from Gimlet Media.",
        "Language": "English",
        "Category": [
            {"Name":"Business", "mark_as_deleted": False}
        ],
        "Website": "http://thepitch.show",
        "Author": "Gimlet Media",
        "Rating": "4.1"
    },
    {
        "ID": "30",
        "Title": "Note to Self",
        "Image": "http://is3.mzstatic.com/image/thumb/Music117/v4/80/5d/a2/805da266-48bb-1b35-54f0-1900a831f3a9/source/600x600bb.jpg",
        "Description": "Is your phone watching you? Can wexting make you smarter? Are your kids real? These and other essential quandaries facing anyone trying to preserve their humanity in the digital age. Join host Manoush Zomorodi for your weekly reminder to question everything. _x000D_\n_x000D_\nWNYC Studios is the producer of other leading podcasts, including Radiolab, Death, Sex & Money, Freakonomics Radio and many others.",
        "Language": "English",
        "Category": [
            {"Name":"Tech News", "mark_as_deleted": False},
            {"Name":"Technology", "mark_as_deleted": False}
        ],
        "Website": "http://www.wnyc.org/shows/notetoself",
        "Author": "WNYC Studios",
        "Rating": "4.2"
    }
]

@app.route('/hello')
def hello_world():
   return 'Hello World' 

@app.route('/')
def search():
    global podcasts
    podcast_titles = []
    for i in range(len(podcasts)):
        podcast_titles.append(podcasts[i]["Title"])
    
    fetched_podcasts = podcasts[-10:][::-1]

    return render_template('podcast_searcher.html', podcast_titles=podcast_titles, podcasts=fetched_podcasts, podcast_details=None, create_page=None)


@app.route('/delete_podcast', methods=['GET', 'POST'])
def delete_podcast():
    global podcasts 

    #get the request and format it into JSON
    json_data = request.get_json()

    #get the id passed
    podcastid = json_data["id"]

    #delete the podcast
    for i in range(len(podcasts)):
        if podcasts[i]["ID"] == podcastid:
            del podcasts[i]
            break

    return jsonify(podcastID = podcastid)

@app.route('/fetch_podcasts', methods=['GET', 'POST'])
def fetch_podcasts():
    global podcasts

    json_data = request.get_json()
    fetched_podcasts = []
    search_name = json_data["search_name"]
    for i in range(len(podcasts)):
        if search_name.lower() in podcasts[i]["Title"].lower():
            fetched_podcasts.append(podcasts[i])
    return jsonify(podcasts = fetched_podcasts)

@app.route('/view/<id>', methods=['GET', 'POST'])
def view_podcast(id=None):
    global podcasts
    chosen_podcast = []
    #get podcast titles
    podcast_titles = []
    for i in range(len(podcasts)):
        podcast_titles.append(podcasts[i]["Title"])
    #find the podcast selected by the user
    for i in range(len(podcasts)):
        if podcasts[i]["ID"] == id:
            chosen_podcast.append(podcasts[i])
    return jsonify(chosen_podcast = chosen_podcast)
    #return jsonify(podcasts = fetched_podcasts)

@app.route('/create', methods=['GET', 'POST'])
def new_podcast(id=None):
    global podcasts
    
    #get podcast titles
    podcast_titles = []
    for i in range(len(podcasts)):
        podcast_titles.append(podcasts[i]["Title"])

    create_page = [{"create_page":"yes"}]
    return render_template('podcast_searcher.html', podcast_titles=podcast_titles, podcasts=None, podcast_details=None, create_page=create_page)
    #return jsonify(podcasts = fetched_podcasts)

@app.route('/add_podcast', methods=['GET', 'POST'])
def add_podcast(id=None):
    global podcasts
    global current_id 

    json_data = request.get_json()
    #app.logger.info('Hello')
    #app.logger.info('json data: %s', json_data)
    title = json_data["Title"]
    author = json_data["Author"]
    website = json_data["Website"]
    image = json_data["Image"]
    language = json_data["Language"]
    description = json_data["Description"]
    rating = json_data["Rating"]
    raw_categories = json_data["Category"]
    categories = raw_categories.split(",")
    for i in range(len(categories)):
        categories[i] = {"Name": categories[i].strip(), "mark_as_deleted": False}
    
    # add new entry to array with 
    # a new id and the name the user sent in JSON
    current_id += 1
    new_id = str(current_id) 
    new_podcast_entry = {
        "ID" : new_id,
        "Title": title,
        "Author": author,
        "Website": website,
        "Image":  image,
        "Language" : language,
        "Description" : description,
        "Rating": rating,
        "Category": categories
    }
    #data.append(new_name_entry)
    podcasts.append(new_podcast_entry)

    podcast_titles = []
    for i in range(len(podcasts)):
        podcast_titles.append(podcasts[i]["Title"])

    return jsonify(podcast_details=[new_podcast_entry], podcast_titles = podcast_titles)

@app.route('/update_podcast', methods=['GET', 'POST'])
def update_podcast():
    global podcasts
    chosen_podcast = []
    json_data = request.get_json()
    description = None
    website = None
    if "Description" in json_data.keys():
        description = json_data["Description"]
    if "Website" in json_data.keys():
        website = json_data["Website"]
    podcast_id = json_data["ID"]
    #find the podcast selected by the user
    for i in range(len(podcasts)):
        if podcasts[i]["ID"] == podcast_id:
            if description != None:
                podcasts[i]["Description"] = description
            if website != None:
                podcasts[i]["Website"] = website
            chosen_podcast.append(podcasts[i])            
    return jsonify(chosen_podcast = chosen_podcast)

@app.route('/update_category', methods=['GET', 'POST'])
def update_category():
    global podcasts
    chosen_podcast = []
    json_data = request.get_json()
    category_name = json_data["Category"]
    podcast_id = json_data["ID"]
    marked_as_deleted = json_data["marked_as_deleted"]
    #find the podcast selected by the user
    for i in range(len(podcasts)):
        if podcasts[i]["ID"] == podcast_id:
            for j in range(len(podcasts[i]["Category"])):
                if podcasts[i]["Category"][j]["Name"] == category_name:
                    podcasts[i]["Category"][j]["marked_as_deleted"] = marked_as_deleted
            chosen_podcast.append(podcasts[i])            
    return jsonify(chosen_podcast = chosen_podcast)

if __name__ == '__main__':
   app.run(debug = True)




