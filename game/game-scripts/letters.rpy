init python:

    class Letter:
        def __init__(self, author="", title="", text="", yuri_2=False, yuri_3=False, alice_2=False):
            self.author = author
            self.title = title
            self.text = text
            self.yuri_2 = yuri_2
            self.yuri_3 = yuri_3
            self.alice_2 = alice_2

    # TODO: Have this written preferrably yby a female.
    letter_1=Letter(
    author = "alice",
    text = """\
    Hi Sayori,

    This is Alice from Joey Drew Studios, the creator of the Bendy and the beautiful Alice Angel cartoons (tee-hee). We have close ties with your high school and have heard from them regarding a literature club being formed. On the behalf of the studio, we're absolutely "stoked" to hear that (is that what the kids say nowadays?)! We've always been a fan of literature here at the studio; our team of writers just {i}love{/i} writing cutesy cartoons of our favorite beautiful angel and dancing ink demon.

    We'd be more than happy to support you and your club! I think it'd be nice to settle for some tea in the studio and discuss plans of sponsorship. There's a new chapter embarking here at the studio since I'm the one running the show now. We're massively revamping the place so it feels more modern, and we are certainly pushing out more cartoons! Sadly, we can't reach Henry, so we've been pushing out more Alice cartoons for the time being. You could probably stay at the studio for a week, if you wanted to, ahaha~! We'll make sure you have a good time.

    We have a lot happening at the studio, and we're more than happy to show you all of the wonderful, beautiful work we've made! We have so many great things, and it'd be a real honor to show you and your members!

    I hope to see you soon!

    - Alice Angel
    """
    )

# Show letter function
label showletter(poem=None, music=False, track=None, revert_music=True, img=None, where=i11, paper=None):
    if poem == None:
        return
    play sound page_turn
    window hide
    $ renpy.game.preferences.afm_enable = False
    if paper:
        show screen poem(poem, paper=paper)
    else:
        show screen poem(poem)
    if not persistent.first_poem:
        $ persistent.first_poem = True
        $ renpy.save_persistent()
        show expression "gui/poem_dismiss.png" as poem_dismiss:
            xpos 1050 ypos 590
    with Dissolve(1)
    $ pause()
    if img:
        $ renpy.hide(poem.author)
        $ renpy.show(img, at_list=[where])
    hide screen poem
    hide poem_dismiss
    with Dissolve(.5)
    window auto
    return
