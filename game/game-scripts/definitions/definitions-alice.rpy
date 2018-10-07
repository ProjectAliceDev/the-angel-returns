## Alice Angel
## Note: The '0' indicates the original sprite modifications as by BippityZop.
## The 'b' in front of '0' will indicate whether she is disfigured or not.
## Any other integer indicates sprites made from Project Scotia.

image alice mesh = "mod_assets/images/alice/old/mesh.png"
image alice 0a = "mod_assets/images/alice/old/a.png"
image alice 0b = "mod_assets/images/alice/old/b.png"
image alice 0c = "mod_assets/images/alice/old/c.png"
image alice 0d = "mod_assets/images/alice/old/d.png"
image alice 0e = "mod_assets/images/alice/old/e.png"
image alice 0f = "mod_assets/images/alice/old/f.png"
image alice 0g = "mod_assets/images/alice/old/g.png"
image alice 0h = "mod_assets/images/alice/old/h.png"
image alice 0i = "mod_assets/images/alice/old/i.png"
image alice 0j = "mod_assets/images/alice/old/j.png"
image alice 0k = "mod_assets/images/alice/old/k.png"
image alice 0l = "mod_assets/images/alice/old/l.png"
image alice 0m = "mod_assets/images/alice/old/m.png"
image alice 0n = "mod_assets/images/alice/old/n.png"
image alice 0o = "mod_assets/images/alice/old/o.png"
image alice 0p = "mod_assets/images/alice/old/p.png"
image alice 0q = "mod_assets/images/alice/old/q.png"
image alice 0r = "mod_assets/images/alice/old/r.png"
image alice 0s = "mod_assets/images/alice/old/s.png"
image alice 0t = "mod_assets/images/alice/old/t.png"
image alice 0u = "mod_assets/images/alice/old/u.png"

image alice 0ba = im.Composite((960,960), (0,0), "mod_assets/images/alice/old/a.png", (0,0), "mod_assets/images/alice/old/susie.png")
image alice 0bb = im.Composite((960,960), (0,0), "mod_assets/images/alice/old/b.png", (0,0), "mod_assets/images/alice/old/susie.png")
image alice 0bc = im.Composite((960,960), (0,0), "mod_assets/images/alice/old/c.png", (0,0), "mod_assets/images/alice/old/susie.png")
image alice 0bd = im.Composite((960,960), (0,0), "mod_assets/images/alice/old/d.png", (0,0), "mod_assets/images/alice/old/susie.png")
image alice 0be = im.Composite((960,960), (0,0), "mod_assets/images/alice/old/e.png", (0,0), "mod_assets/images/alice/old/susie.png")
image alice 0bf = im.Composite((960,960), (0,0), "mod_assets/images/alice/old/f.png", (0,0), "mod_assets/images/alice/old/susie.png")
image alice 0bg = im.Composite((960,960), (0,0), "mod_assets/images/alice/old/g.png", (0,0), "mod_assets/images/alice/old/susie.png")
image alice 0bh = im.Composite((960,960), (0,0), "mod_assets/images/alice/old/h.png", (0,0), "mod_assets/images/alice/old/susie.png")
image alice 0bi = im.Composite((960,960), (0,0), "mod_assets/images/alice/old/i.png", (0,0), "mod_assets/images/alice/old/susie.png")
image alice 0bj = im.Composite((960,960), (0,0), "mod_assets/images/alice/old/j.png", (0,0), "mod_assets/images/alice/old/susie.png")
image alice 0bk = im.Composite((960,960), (0,0), "mod_assets/images/alice/old/k.png", (0,0), "mod_assets/images/alice/old/susie.png")
image alice 0bl = im.Composite((960,960), (0,0), "mod_assets/images/alice/old/l.png", (0,0), "mod_assets/images/alice/old/susie.png")
image alice 0bm = im.Composite((960,960), (0,0), "mod_assets/images/alice/old/m.png", (0,0), "mod_assets/images/alice/old/susie.png")
image alice 0bn = im.Composite((960,960), (0,0), "mod_assets/images/alice/old/n.png", (0,0), "mod_assets/images/alice/old/susie.png")
image alice 0bo = im.Composite((960,960), (0,0), "mod_assets/images/alice/old/o.png", (0,0), "mod_assets/images/alice/old/susie.png")
image alice 0bp = im.Composite((960,960), (0,0), "mod_assets/images/alice/old/p.png", (0,0), "mod_assets/images/alice/old/susie.png")
image alice 0bq = im.Composite((960,960), (0,0), "mod_assets/images/alice/old/q.png", (0,0), "mod_assets/images/alice/old/susie.png")
image alice 0br = im.Composite((960,960), (0,0), "mod_assets/images/alice/old/r.png", (0,0), "mod_assets/images/alice/old/susie.png")
image alice 0bs = im.Composite((960,960), (0,0), "mod_assets/images/alice/old/s.png", (0,0), "mod_assets/images/alice/old/susie.png")
image alice 0bt = im.Composite((960,960), (0,0), "mod_assets/images/alice/old/t.png", (0,0), "mod_assets/images/alice/old/susie.png")
image alice 0bu = im.Composite((960,960), (0,0), "mod_assets/images/alice/old/u.png", (0,0), "mod_assets/images/alice/old/susie.png")


image alice eyes = LiveComposite((1280, 720), (0, 0), "mod_assets/images/alice/old/eyes1.png", (0, 0), "alicepupils")

image alice eyes_base = "mod_assets/images/alice/old/eyes1.png"

image alicepupils:
    "mod_assets/images/alice/old/eyes2.png"
    yuripupils_move

image alice glitch:
    block:
        choice:
            "mod_assets/images/alice/old/glitch1.png"
        choice:
            "mod_assets/images/alice/old/glitch2.png"
        choice:
            "mod_assets/images/alice/old/glitch3.png"
    block:
        choice:
            pause 0.05
        choice:
            pause 0.1
        choice:
            pause 0.15
        choice:
            pause 0.2
    repeat

## Project Scotia sprites
# These are the new sprites to present the official Alice in-game.
# Using "s" after the digit will indicate the deform face function.
# Using "b" after the digit and/or the "s" will indicate casual wear.

image alice 1 = im.Composite((960,960), (0,0), "mod_assets/images/alice/1l.png", (0,0), "mod_assets/images/alice/1r.png", (0,0), "mod_assets/images/alice/a.png")

image alice 1a = im.Composite((960,960), (0,0), "mod_assets/images/alice/1l.png", (0,0), "mod_assets/images/alice/1r.png", (0,0), "mod_assets/images/alice/a.png")
image alice 1sa = im.Composite((960,960), (0,0), "mod_assets/images/alice/1l.png", (0,0), "mod_assets/images/alice/1r.png", (0,0), "mod_assets/images/alice/a.png", (0,0), "mod_assets/images/alice/deform.png")