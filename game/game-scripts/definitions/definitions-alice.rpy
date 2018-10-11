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
image alice 2 = im.Composite((960,960), (0,0), "mod_assets/images/alice/1l.png", (0,0), "mod_assets/images/alice/2r.png", (0,0), "mod_assets/images/alice/a.png")
image alice 3 = im.Composite((960,960), (0,0), "mod_assets/images/alice/2l.png", (0,0), "mod_assets/images/alice/1r.png", (0,0), "mod_assets/images/alice/a.png")
image alice 4 = im.Composite((960,960), (0,0), "mod_assets/images/alice/2l.png", (0,0), "mod_assets/images/alice/2r.png", (0,0), "mod_assets/images/alice/a.png")

image alice 1a = im.Composite((960,960), (0,0), "mod_assets/images/alice/1l.png", (0,0), "mod_assets/images/alice/1r.png", (0,0), "mod_assets/images/alice/a.png")
image alice 1b = im.Composite((960,960), (0,0), "mod_assets/images/alice/1l.png", (0,0), "mod_assets/images/alice/1r.png", (0,0), "mod_assets/images/alice/b.png")
image alice 1c = im.Composite((960,960), (0,0), "mod_assets/images/alice/1l.png", (0,0), "mod_assets/images/alice/1r.png", (0,0), "mod_assets/images/alice/c.png")
image alice 1d = im.Composite((960,960), (0,0), "mod_assets/images/alice/1l.png", (0,0), "mod_assets/images/alice/1r.png", (0,0), "mod_assets/images/alice/d.png")
image alice 1e = im.Composite((960,960), (0,0), "mod_assets/images/alice/1l.png", (0,0), "mod_assets/images/alice/1r.png", (0,0), "mod_assets/images/alice/e.png")
image alice 1f = im.Composite((960,960), (0,0), "mod_assets/images/alice/1l.png", (0,0), "mod_assets/images/alice/1r.png", (0,0), "mod_assets/images/alice/f.png")
image alice 1g = im.Composite((960,960), (0,0), "mod_assets/images/alice/1l.png", (0,0), "mod_assets/images/alice/1r.png", (0,0), "mod_assets/images/alice/g.png")
image alice 1h = im.Composite((960,960), (0,0), "mod_assets/images/alice/1l.png", (0,0), "mod_assets/images/alice/1r.png", (0,0), "mod_assets/images/alice/h.png")
image alice 1i = im.Composite((960,960), (0,0), "mod_assets/images/alice/1l.png", (0,0), "mod_assets/images/alice/1r.png", (0,0), "mod_assets/images/alice/i.png")
image alice 1j = im.Composite((960,960), (0,0), "mod_assets/images/alice/1l.png", (0,0), "mod_assets/images/alice/1r.png", (0,0), "mod_assets/images/alice/j.png")
image alice 1k = im.Composite((960,960), (0,0), "mod_assets/images/alice/1l.png", (0,0), "mod_assets/images/alice/1r.png", (0,0), "mod_assets/images/alice/k.png")
image alice 1l = im.Composite((960,960), (0,0), "mod_assets/images/alice/1l.png", (0,0), "mod_assets/images/alice/1r.png", (0,0), "mod_assets/images/alice/l.png")
image alice 1m = im.Composite((960,960), (0,0), "mod_assets/images/alice/1l.png", (0,0), "mod_assets/images/alice/1r.png", (0,0), "mod_assets/images/alice/m.png")
image alice 1n = im.Composite((960,960), (0,0), "mod_assets/images/alice/1l.png", (0,0), "mod_assets/images/alice/1r.png", (0,0), "mod_assets/images/alice/n.png")
image alice 1o = im.Composite((960,960), (0,0), "mod_assets/images/alice/1l.png", (0,0), "mod_assets/images/alice/1r.png", (0,0), "mod_assets/images/alice/o.png")
image alice 1p = im.Composite((960,960), (0,0), "mod_assets/images/alice/1l.png", (0,0), "mod_assets/images/alice/1r.png", (0,0), "mod_assets/images/alice/p.png")
image alice 1q = im.Composite((960,960), (0,0), "mod_assets/images/alice/1l.png", (0,0), "mod_assets/images/alice/1r.png", (0,0), "mod_assets/images/alice/q.png")
image alice 1r = im.Composite((960,960), (0,0), "mod_assets/images/alice/1l.png", (0,0), "mod_assets/images/alice/1r.png", (0,0), "mod_assets/images/alice/r.png")
image alice 1s = im.Composite((960,960), (0,0), "mod_assets/images/alice/1l.png", (0,0), "mod_assets/images/alice/1r.png", (0,0), "mod_assets/images/alice/s.png")
image alice 1t = im.Composite((960,960), (0,0), "mod_assets/images/alice/1l.png", (0,0), "mod_assets/images/alice/1r.png", (0,0), "mod_assets/images/alice/t.png")
image alice 1u = im.Composite((960,960), (0,0), "mod_assets/images/alice/1l.png", (0,0), "mod_assets/images/alice/1r.png", (0,0), "mod_assets/images/alice/u.png")


image alice 1sa = im.Composite((960,960), (0,0), "mod_assets/images/alice/1l.png", (0,0), "mod_assets/images/alice/1r.png", (0,0), "mod_assets/images/alice/a.png", (0,0), "mod_assets/images/alice/deform.png")
image alice 1sb = im.Composite((960,960), (0,0), "mod_assets/images/alice/1l.png", (0,0), "mod_assets/images/alice/1r.png", (0,0), "mod_assets/images/alice/b.png", (0,0), "mod_assets/images/alice/deform.png")
image alice 1sc = im.Composite((960,960), (0,0), "mod_assets/images/alice/1l.png", (0,0), "mod_assets/images/alice/1r.png", (0,0), "mod_assets/images/alice/c.png", (0,0), "mod_assets/images/alice/deform.png")
image alice 1sd = im.Composite((960,960), (0,0), "mod_assets/images/alice/1l.png", (0,0), "mod_assets/images/alice/1r.png", (0,0), "mod_assets/images/alice/d.png", (0,0), "mod_assets/images/alice/deform.png")
image alice 1se = im.Composite((960,960), (0,0), "mod_assets/images/alice/1l.png", (0,0), "mod_assets/images/alice/1r.png", (0,0), "mod_assets/images/alice/e.png", (0,0), "mod_assets/images/alice/deform.png")
image alice 1sf = im.Composite((960,960), (0,0), "mod_assets/images/alice/1l.png", (0,0), "mod_assets/images/alice/1r.png", (0,0), "mod_assets/images/alice/f.png", (0,0), "mod_assets/images/alice/deform.png")
image alice 1sg = im.Composite((960,960), (0,0), "mod_assets/images/alice/1l.png", (0,0), "mod_assets/images/alice/1r.png", (0,0), "mod_assets/images/alice/g.png", (0,0), "mod_assets/images/alice/deform.png")
image alice 1sh = im.Composite((960,960), (0,0), "mod_assets/images/alice/1l.png", (0,0), "mod_assets/images/alice/1r.png", (0,0), "mod_assets/images/alice/h.png", (0,0), "mod_assets/images/alice/deform.png")
image alice 1si = im.Composite((960,960), (0,0), "mod_assets/images/alice/1l.png", (0,0), "mod_assets/images/alice/1r.png", (0,0), "mod_assets/images/alice/i.png", (0,0), "mod_assets/images/alice/deform.png")
image alice 1sj = im.Composite((960,960), (0,0), "mod_assets/images/alice/1l.png", (0,0), "mod_assets/images/alice/1r.png", (0,0), "mod_assets/images/alice/j.png", (0,0), "mod_assets/images/alice/deform.png")
image alice 1sk = im.Composite((960,960), (0,0), "mod_assets/images/alice/1l.png", (0,0), "mod_assets/images/alice/1r.png", (0,0), "mod_assets/images/alice/k.png", (0,0), "mod_assets/images/alice/deform.png")
image alice 1sl = im.Composite((960,960), (0,0), "mod_assets/images/alice/1l.png", (0,0), "mod_assets/images/alice/1r.png", (0,0), "mod_assets/images/alice/l.png", (0,0), "mod_assets/images/alice/deform.png")
image alice 1sm = im.Composite((960,960), (0,0), "mod_assets/images/alice/1l.png", (0,0), "mod_assets/images/alice/1r.png", (0,0), "mod_assets/images/alice/m.png", (0,0), "mod_assets/images/alice/deform.png")
image alice 1sn = im.Composite((960,960), (0,0), "mod_assets/images/alice/1l.png", (0,0), "mod_assets/images/alice/1r.png", (0,0), "mod_assets/images/alice/n.png", (0,0), "mod_assets/images/alice/deform.png")
image alice 1so = im.Composite((960,960), (0,0), "mod_assets/images/alice/1l.png", (0,0), "mod_assets/images/alice/1r.png", (0,0), "mod_assets/images/alice/o.png", (0,0), "mod_assets/images/alice/deform.png")
image alice 1sp = im.Composite((960,960), (0,0), "mod_assets/images/alice/1l.png", (0,0), "mod_assets/images/alice/1r.png", (0,0), "mod_assets/images/alice/p.png", (0,0), "mod_assets/images/alice/deform.png")
image alice 1sq = im.Composite((960,960), (0,0), "mod_assets/images/alice/1l.png", (0,0), "mod_assets/images/alice/1r.png", (0,0), "mod_assets/images/alice/q.png", (0,0), "mod_assets/images/alice/deformy.png")
image alice 1sr = im.Composite((960,960), (0,0), "mod_assets/images/alice/1l.png", (0,0), "mod_assets/images/alice/1r.png", (0,0), "mod_assets/images/alice/r.png", (0,0), "mod_assets/images/alice/deformy.png")
image alice 1ss = im.Composite((960,960), (0,0), "mod_assets/images/alice/1l.png", (0,0), "mod_assets/images/alice/1r.png", (0,0), "mod_assets/images/alice/s.png", (0,0), "mod_assets/images/alice/deformy.png")
image alice 1st = im.Composite((960,960), (0,0), "mod_assets/images/alice/1l.png", (0,0), "mod_assets/images/alice/1r.png", (0,0), "mod_assets/images/alice/t.png", (0,0), "mod_assets/images/alice/deformy.png")
image alice 1su = im.Composite((960,960), (0,0), "mod_assets/images/alice/1l.png", (0,0), "mod_assets/images/alice/1r.png", (0,0), "mod_assets/images/alice/u.png", (0,0), "mod_assets/images/alice/deformy.png")



image alice 1y1 = im.Composite((960,960), (0,0), "mod_assets/images/alice/1l.png", (0,0), "mod_assets/images/alice/1r.png", (0,0), "mod_assets/images/alice/y1.png")
image alice 1y2 = im.Composite((960,960), (0,0), "mod_assets/images/alice/1l.png", (0,0), "mod_assets/images/alice/1r.png", (0,0), "mod_assets/images/alice/y2.png")
image alice 1y3 = im.Composite((960,960), (0,0), "mod_assets/images/alice/1l.png", (0,0), "mod_assets/images/alice/1r.png", (0,0), "mod_assets/images/alice/y3.png")
image alice 1y4 = im.Composite((960,960), (0,0), "mod_assets/images/alice/1l.png", (0,0), "mod_assets/images/alice/1r.png", (0,0), "mod_assets/images/alice/y4.png")
image alice 1y5 = im.Composite((960,960), (0,0), "mod_assets/images/alice/1l.png", (0,0), "mod_assets/images/alice/1r.png", (0,0), "mod_assets/images/alice/y5.png")


image alice 1sy1 = im.Composite((960,960), (0,0), "mod_assets/images/alice/1l.png", (0,0), "mod_assets/images/alice/1r.png", (0,0), "mod_assets/images/alice/y1.png", (0,0), "mod_assets/images/alice/deformy.png")
image alice 1sy2 = im.Composite((960,960), (0,0), "mod_assets/images/alice/1l.png", (0,0), "mod_assets/images/alice/1r.png", (0,0), "mod_assets/images/alice/y2.png", (0,0), "mod_assets/images/alice/deformy.png")
image alice 1sy3 = im.Composite((960,960), (0,0), "mod_assets/images/alice/1l.png", (0,0), "mod_assets/images/alice/1r.png", (0,0), "mod_assets/images/alice/y3.png", (0,0), "mod_assets/images/alice/deformy.png")
image alice 1sy4 = im.Composite((960,960), (0,0), "mod_assets/images/alice/1l.png", (0,0), "mod_assets/images/alice/1r.png", (0,0), "mod_assets/images/alice/y4.png", (0,0), "mod_assets/images/alice/deformy.png")
image alice 1sy5 = im.Composite((960,960), (0,0), "mod_assets/images/alice/1l.png", (0,0), "mod_assets/images/alice/1r.png", (0,0), "mod_assets/images/alice/y5.png", (0,0), "mod_assets/images/alice/deformy.png")






image alice 2a = im.Composite((960,960), (0,0), "mod_assets/images/alice/1l.png", (0,0), "mod_assets/images/alice/2r.png", (0,0), "mod_assets/images/alice/a.png")
image alice 2b = im.Composite((960,960), (0,0), "mod_assets/images/alice/1l.png", (0,0), "mod_assets/images/alice/2r.png", (0,0), "mod_assets/images/alice/b.png")
image alice 2c = im.Composite((960,960), (0,0), "mod_assets/images/alice/1l.png", (0,0), "mod_assets/images/alice/2r.png", (0,0), "mod_assets/images/alice/c.png")
image alice 2d = im.Composite((960,960), (0,0), "mod_assets/images/alice/1l.png", (0,0), "mod_assets/images/alice/2r.png", (0,0), "mod_assets/images/alice/d.png")
image alice 2e = im.Composite((960,960), (0,0), "mod_assets/images/alice/1l.png", (0,0), "mod_assets/images/alice/2r.png", (0,0), "mod_assets/images/alice/e.png")
image alice 2f = im.Composite((960,960), (0,0), "mod_assets/images/alice/1l.png", (0,0), "mod_assets/images/alice/2r.png", (0,0), "mod_assets/images/alice/f.png")
image alice 2g = im.Composite((960,960), (0,0), "mod_assets/images/alice/1l.png", (0,0), "mod_assets/images/alice/2r.png", (0,0), "mod_assets/images/alice/g.png")
image alice 2h = im.Composite((960,960), (0,0), "mod_assets/images/alice/1l.png", (0,0), "mod_assets/images/alice/2r.png", (0,0), "mod_assets/images/alice/h.png")
image alice 2i = im.Composite((960,960), (0,0), "mod_assets/images/alice/1l.png", (0,0), "mod_assets/images/alice/2r.png", (0,0), "mod_assets/images/alice/i.png")
image alice 2j = im.Composite((960,960), (0,0), "mod_assets/images/alice/1l.png", (0,0), "mod_assets/images/alice/2r.png", (0,0), "mod_assets/images/alice/j.png")
image alice 2k = im.Composite((960,960), (0,0), "mod_assets/images/alice/1l.png", (0,0), "mod_assets/images/alice/2r.png", (0,0), "mod_assets/images/alice/k.png")
image alice 2l = im.Composite((960,960), (0,0), "mod_assets/images/alice/1l.png", (0,0), "mod_assets/images/alice/2r.png", (0,0), "mod_assets/images/alice/l.png")
image alice 2m = im.Composite((960,960), (0,0), "mod_assets/images/alice/1l.png", (0,0), "mod_assets/images/alice/2r.png", (0,0), "mod_assets/images/alice/m.png")
image alice 2n = im.Composite((960,960), (0,0), "mod_assets/images/alice/1l.png", (0,0), "mod_assets/images/alice/2r.png", (0,0), "mod_assets/images/alice/n.png")
image alice 2o = im.Composite((960,960), (0,0), "mod_assets/images/alice/1l.png", (0,0), "mod_assets/images/alice/2r.png", (0,0), "mod_assets/images/alice/o.png")
image alice 2p = im.Composite((960,960), (0,0), "mod_assets/images/alice/1l.png", (0,0), "mod_assets/images/alice/2r.png", (0,0), "mod_assets/images/alice/p.png")
image alice 2q = im.Composite((960,960), (0,0), "mod_assets/images/alice/1l.png", (0,0), "mod_assets/images/alice/2r.png", (0,0), "mod_assets/images/alice/q.png")
image alice 2r = im.Composite((960,960), (0,0), "mod_assets/images/alice/1l.png", (0,0), "mod_assets/images/alice/2r.png", (0,0), "mod_assets/images/alice/r.png")
image alice 2s = im.Composite((960,960), (0,0), "mod_assets/images/alice/1l.png", (0,0), "mod_assets/images/alice/2r.png", (0,0), "mod_assets/images/alice/s.png")
image alice 2t = im.Composite((960,960), (0,0), "mod_assets/images/alice/1l.png", (0,0), "mod_assets/images/alice/2r.png", (0,0), "mod_assets/images/alice/t.png")
image alice 2u = im.Composite((960,960), (0,0), "mod_assets/images/alice/1l.png", (0,0), "mod_assets/images/alice/2r.png", (0,0), "mod_assets/images/alice/u.png")


image alice 2sa = im.Composite((960,960), (0,0), "mod_assets/images/alice/1l.png", (0,0), "mod_assets/images/alice/2r.png", (0,0), "mod_assets/images/alice/a.png", (0,0), "mod_assets/images/alice/deform.png")
image alice 2sb = im.Composite((960,960), (0,0), "mod_assets/images/alice/1l.png", (0,0), "mod_assets/images/alice/2r.png", (0,0), "mod_assets/images/alice/b.png", (0,0), "mod_assets/images/alice/deform.png")
image alice 2sc = im.Composite((960,960), (0,0), "mod_assets/images/alice/1l.png", (0,0), "mod_assets/images/alice/2r.png", (0,0), "mod_assets/images/alice/c.png", (0,0), "mod_assets/images/alice/deform.png")
image alice 2sd = im.Composite((960,960), (0,0), "mod_assets/images/alice/1l.png", (0,0), "mod_assets/images/alice/2r.png", (0,0), "mod_assets/images/alice/d.png", (0,0), "mod_assets/images/alice/deform.png")
image alice 2se = im.Composite((960,960), (0,0), "mod_assets/images/alice/1l.png", (0,0), "mod_assets/images/alice/2r.png", (0,0), "mod_assets/images/alice/e.png", (0,0), "mod_assets/images/alice/deform.png")
image alice 2sf = im.Composite((960,960), (0,0), "mod_assets/images/alice/1l.png", (0,0), "mod_assets/images/alice/2r.png", (0,0), "mod_assets/images/alice/f.png", (0,0), "mod_assets/images/alice/deform.png")
image alice 2sg = im.Composite((960,960), (0,0), "mod_assets/images/alice/1l.png", (0,0), "mod_assets/images/alice/2r.png", (0,0), "mod_assets/images/alice/g.png", (0,0), "mod_assets/images/alice/deform.png")
image alice 2sh = im.Composite((960,960), (0,0), "mod_assets/images/alice/1l.png", (0,0), "mod_assets/images/alice/2r.png", (0,0), "mod_assets/images/alice/h.png", (0,0), "mod_assets/images/alice/deform.png")
image alice 2si = im.Composite((960,960), (0,0), "mod_assets/images/alice/1l.png", (0,0), "mod_assets/images/alice/2r.png", (0,0), "mod_assets/images/alice/i.png", (0,0), "mod_assets/images/alice/deform.png")
image alice 2sj = im.Composite((960,960), (0,0), "mod_assets/images/alice/1l.png", (0,0), "mod_assets/images/alice/2r.png", (0,0), "mod_assets/images/alice/j.png", (0,0), "mod_assets/images/alice/deform.png")
image alice 2sk = im.Composite((960,960), (0,0), "mod_assets/images/alice/1l.png", (0,0), "mod_assets/images/alice/2r.png", (0,0), "mod_assets/images/alice/k.png", (0,0), "mod_assets/images/alice/deform.png")
image alice 2sl = im.Composite((960,960), (0,0), "mod_assets/images/alice/1l.png", (0,0), "mod_assets/images/alice/2r.png", (0,0), "mod_assets/images/alice/l.png", (0,0), "mod_assets/images/alice/deform.png")
image alice 2sm = im.Composite((960,960), (0,0), "mod_assets/images/alice/1l.png", (0,0), "mod_assets/images/alice/2r.png", (0,0), "mod_assets/images/alice/m.png", (0,0), "mod_assets/images/alice/deform.png")
image alice 2sn = im.Composite((960,960), (0,0), "mod_assets/images/alice/1l.png", (0,0), "mod_assets/images/alice/2r.png", (0,0), "mod_assets/images/alice/n.png", (0,0), "mod_assets/images/alice/deform.png")
image alice 2so = im.Composite((960,960), (0,0), "mod_assets/images/alice/1l.png", (0,0), "mod_assets/images/alice/2r.png", (0,0), "mod_assets/images/alice/o.png", (0,0), "mod_assets/images/alice/deform.png")
image alice 2sp = im.Composite((960,960), (0,0), "mod_assets/images/alice/1l.png", (0,0), "mod_assets/images/alice/2r.png", (0,0), "mod_assets/images/alice/p.png", (0,0), "mod_assets/images/alice/deform.png")
image alice 2sq = im.Composite((960,960), (0,0), "mod_assets/images/alice/1l.png", (0,0), "mod_assets/images/alice/2r.png", (0,0), "mod_assets/images/alice/q.png", (0,0), "mod_assets/images/alice/deformy.png")
image alice 2sr = im.Composite((960,960), (0,0), "mod_assets/images/alice/1l.png", (0,0), "mod_assets/images/alice/2r.png", (0,0), "mod_assets/images/alice/r.png", (0,0), "mod_assets/images/alice/deformy.png")
image alice 2ss = im.Composite((960,960), (0,0), "mod_assets/images/alice/1l.png", (0,0), "mod_assets/images/alice/2r.png", (0,0), "mod_assets/images/alice/s.png", (0,0), "mod_assets/images/alice/deformy.png")
image alice 2st = im.Composite((960,960), (0,0), "mod_assets/images/alice/1l.png", (0,0), "mod_assets/images/alice/2r.png", (0,0), "mod_assets/images/alice/t.png", (0,0), "mod_assets/images/alice/deformy.png")
image alice 2su = im.Composite((960,960), (0,0), "mod_assets/images/alice/1l.png", (0,0), "mod_assets/images/alice/2r.png", (0,0), "mod_assets/images/alice/u.png", (0,0), "mod_assets/images/alice/deformy.png")



image alice 2y1 = im.Composite((960,960), (0,0), "mod_assets/images/alice/1l.png", (0,0), "mod_assets/images/alice/2r.png", (0,0), "mod_assets/images/alice/y1.png")
image alice 2y2 = im.Composite((960,960), (0,0), "mod_assets/images/alice/1l.png", (0,0), "mod_assets/images/alice/2r.png", (0,0), "mod_assets/images/alice/y2.png")
image alice 2y3 = im.Composite((960,960), (0,0), "mod_assets/images/alice/1l.png", (0,0), "mod_assets/images/alice/2r.png", (0,0), "mod_assets/images/alice/y3.png")
image alice 2y4 = im.Composite((960,960), (0,0), "mod_assets/images/alice/1l.png", (0,0), "mod_assets/images/alice/2r.png", (0,0), "mod_assets/images/alice/y4.png")
image alice 2y5 = im.Composite((960,960), (0,0), "mod_assets/images/alice/1l.png", (0,0), "mod_assets/images/alice/2r.png", (0,0), "mod_assets/images/alice/y5.png")


image alice 2sy1 = im.Composite((960,960), (0,0), "mod_assets/images/alice/1l.png", (0,0), "mod_assets/images/alice/2r.png", (0,0), "mod_assets/images/alice/y1.png", (0,0), "mod_assets/images/alice/deformy.png")
image alice 2sy2 = im.Composite((960,960), (0,0), "mod_assets/images/alice/1l.png", (0,0), "mod_assets/images/alice/2r.png", (0,0), "mod_assets/images/alice/y2.png", (0,0), "mod_assets/images/alice/deformy.png")
image alice 2sy3 = im.Composite((960,960), (0,0), "mod_assets/images/alice/1l.png", (0,0), "mod_assets/images/alice/2r.png", (0,0), "mod_assets/images/alice/y3.png", (0,0), "mod_assets/images/alice/deformy.png")
image alice 2sy4 = im.Composite((960,960), (0,0), "mod_assets/images/alice/1l.png", (0,0), "mod_assets/images/alice/2r.png", (0,0), "mod_assets/images/alice/y4.png", (0,0), "mod_assets/images/alice/deformy.png")
image alice 2sy5 = im.Composite((960,960), (0,0), "mod_assets/images/alice/1l.png", (0,0), "mod_assets/images/alice/2r.png", (0,0), "mod_assets/images/alice/y5.png", (0,0), "mod_assets/images/alice/deformy.png")






image alice 3a = im.Composite((960,960), (0,0), "mod_assets/images/alice/2l.png", (0,0), "mod_assets/images/alice/1r.png", (0,0), "mod_assets/images/alice/a.png")
image alice 3b = im.Composite((960,960), (0,0), "mod_assets/images/alice/2l.png", (0,0), "mod_assets/images/alice/1r.png", (0,0), "mod_assets/images/alice/b.png")
image alice 3c = im.Composite((960,960), (0,0), "mod_assets/images/alice/2l.png", (0,0), "mod_assets/images/alice/1r.png", (0,0), "mod_assets/images/alice/c.png")
image alice 3d = im.Composite((960,960), (0,0), "mod_assets/images/alice/2l.png", (0,0), "mod_assets/images/alice/1r.png", (0,0), "mod_assets/images/alice/d.png")
image alice 3e = im.Composite((960,960), (0,0), "mod_assets/images/alice/2l.png", (0,0), "mod_assets/images/alice/1r.png", (0,0), "mod_assets/images/alice/e.png")
image alice 3f = im.Composite((960,960), (0,0), "mod_assets/images/alice/2l.png", (0,0), "mod_assets/images/alice/1r.png", (0,0), "mod_assets/images/alice/f.png")
image alice 3g = im.Composite((960,960), (0,0), "mod_assets/images/alice/2l.png", (0,0), "mod_assets/images/alice/1r.png", (0,0), "mod_assets/images/alice/g.png")
image alice 3h = im.Composite((960,960), (0,0), "mod_assets/images/alice/2l.png", (0,0), "mod_assets/images/alice/1r.png", (0,0), "mod_assets/images/alice/h.png")
image alice 3i = im.Composite((960,960), (0,0), "mod_assets/images/alice/2l.png", (0,0), "mod_assets/images/alice/1r.png", (0,0), "mod_assets/images/alice/i.png")
image alice 3j = im.Composite((960,960), (0,0), "mod_assets/images/alice/2l.png", (0,0), "mod_assets/images/alice/1r.png", (0,0), "mod_assets/images/alice/j.png")
image alice 3k = im.Composite((960,960), (0,0), "mod_assets/images/alice/2l.png", (0,0), "mod_assets/images/alice/1r.png", (0,0), "mod_assets/images/alice/k.png")
image alice 3l = im.Composite((960,960), (0,0), "mod_assets/images/alice/2l.png", (0,0), "mod_assets/images/alice/1r.png", (0,0), "mod_assets/images/alice/l.png")
image alice 3m = im.Composite((960,960), (0,0), "mod_assets/images/alice/2l.png", (0,0), "mod_assets/images/alice/1r.png", (0,0), "mod_assets/images/alice/m.png")
image alice 3n = im.Composite((960,960), (0,0), "mod_assets/images/alice/2l.png", (0,0), "mod_assets/images/alice/1r.png", (0,0), "mod_assets/images/alice/n.png")
image alice 3o = im.Composite((960,960), (0,0), "mod_assets/images/alice/2l.png", (0,0), "mod_assets/images/alice/1r.png", (0,0), "mod_assets/images/alice/o.png")
image alice 3p = im.Composite((960,960), (0,0), "mod_assets/images/alice/2l.png", (0,0), "mod_assets/images/alice/1r.png", (0,0), "mod_assets/images/alice/p.png")
image alice 3q = im.Composite((960,960), (0,0), "mod_assets/images/alice/2l.png", (0,0), "mod_assets/images/alice/1r.png", (0,0), "mod_assets/images/alice/q.png")
image alice 3r = im.Composite((960,960), (0,0), "mod_assets/images/alice/2l.png", (0,0), "mod_assets/images/alice/1r.png", (0,0), "mod_assets/images/alice/r.png")
image alice 3s = im.Composite((960,960), (0,0), "mod_assets/images/alice/2l.png", (0,0), "mod_assets/images/alice/1r.png", (0,0), "mod_assets/images/alice/s.png")
image alice 3t = im.Composite((960,960), (0,0), "mod_assets/images/alice/2l.png", (0,0), "mod_assets/images/alice/1r.png", (0,0), "mod_assets/images/alice/t.png")
image alice 3u = im.Composite((960,960), (0,0), "mod_assets/images/alice/2l.png", (0,0), "mod_assets/images/alice/1r.png", (0,0), "mod_assets/images/alice/u.png")


image alice 3sa = im.Composite((960,960), (0,0), "mod_assets/images/alice/2l.png", (0,0), "mod_assets/images/alice/1r.png", (0,0), "mod_assets/images/alice/a.png", (0,0), "mod_assets/images/alice/deform.png")
image alice 3sb = im.Composite((960,960), (0,0), "mod_assets/images/alice/2l.png", (0,0), "mod_assets/images/alice/1r.png", (0,0), "mod_assets/images/alice/b.png", (0,0), "mod_assets/images/alice/deform.png")
image alice 3sc = im.Composite((960,960), (0,0), "mod_assets/images/alice/2l.png", (0,0), "mod_assets/images/alice/1r.png", (0,0), "mod_assets/images/alice/c.png", (0,0), "mod_assets/images/alice/deform.png")
image alice 3sd = im.Composite((960,960), (0,0), "mod_assets/images/alice/2l.png", (0,0), "mod_assets/images/alice/1r.png", (0,0), "mod_assets/images/alice/d.png", (0,0), "mod_assets/images/alice/deform.png")
image alice 3se = im.Composite((960,960), (0,0), "mod_assets/images/alice/2l.png", (0,0), "mod_assets/images/alice/1r.png", (0,0), "mod_assets/images/alice/e.png", (0,0), "mod_assets/images/alice/deform.png")
image alice 3sf = im.Composite((960,960), (0,0), "mod_assets/images/alice/2l.png", (0,0), "mod_assets/images/alice/1r.png", (0,0), "mod_assets/images/alice/f.png", (0,0), "mod_assets/images/alice/deform.png")
image alice 3sg = im.Composite((960,960), (0,0), "mod_assets/images/alice/2l.png", (0,0), "mod_assets/images/alice/1r.png", (0,0), "mod_assets/images/alice/g.png", (0,0), "mod_assets/images/alice/deform.png")
image alice 3sh = im.Composite((960,960), (0,0), "mod_assets/images/alice/2l.png", (0,0), "mod_assets/images/alice/1r.png", (0,0), "mod_assets/images/alice/h.png", (0,0), "mod_assets/images/alice/deform.png")
image alice 3si = im.Composite((960,960), (0,0), "mod_assets/images/alice/2l.png", (0,0), "mod_assets/images/alice/1r.png", (0,0), "mod_assets/images/alice/i.png", (0,0), "mod_assets/images/alice/deform.png")
image alice 3sj = im.Composite((960,960), (0,0), "mod_assets/images/alice/2l.png", (0,0), "mod_assets/images/alice/1r.png", (0,0), "mod_assets/images/alice/j.png", (0,0), "mod_assets/images/alice/deform.png")
image alice 3sk = im.Composite((960,960), (0,0), "mod_assets/images/alice/2l.png", (0,0), "mod_assets/images/alice/1r.png", (0,0), "mod_assets/images/alice/k.png", (0,0), "mod_assets/images/alice/deform.png")
image alice 3sl = im.Composite((960,960), (0,0), "mod_assets/images/alice/2l.png", (0,0), "mod_assets/images/alice/1r.png", (0,0), "mod_assets/images/alice/l.png", (0,0), "mod_assets/images/alice/deform.png")
image alice 3sm = im.Composite((960,960), (0,0), "mod_assets/images/alice/2l.png", (0,0), "mod_assets/images/alice/1r.png", (0,0), "mod_assets/images/alice/m.png", (0,0), "mod_assets/images/alice/deform.png")
image alice 3sn = im.Composite((960,960), (0,0), "mod_assets/images/alice/2l.png", (0,0), "mod_assets/images/alice/1r.png", (0,0), "mod_assets/images/alice/n.png", (0,0), "mod_assets/images/alice/deform.png")
image alice 3so = im.Composite((960,960), (0,0), "mod_assets/images/alice/2l.png", (0,0), "mod_assets/images/alice/1r.png", (0,0), "mod_assets/images/alice/o.png", (0,0), "mod_assets/images/alice/deform.png")
image alice 3sp = im.Composite((960,960), (0,0), "mod_assets/images/alice/2l.png", (0,0), "mod_assets/images/alice/1r.png", (0,0), "mod_assets/images/alice/p.png", (0,0), "mod_assets/images/alice/deform.png")
image alice 3sq = im.Composite((960,960), (0,0), "mod_assets/images/alice/2l.png", (0,0), "mod_assets/images/alice/1r.png", (0,0), "mod_assets/images/alice/q.png", (0,0), "mod_assets/images/alice/deformy.png")
image alice 3sr = im.Composite((960,960), (0,0), "mod_assets/images/alice/2l.png", (0,0), "mod_assets/images/alice/1r.png", (0,0), "mod_assets/images/alice/r.png", (0,0), "mod_assets/images/alice/deformy.png")
image alice 3ss = im.Composite((960,960), (0,0), "mod_assets/images/alice/2l.png", (0,0), "mod_assets/images/alice/1r.png", (0,0), "mod_assets/images/alice/s.png", (0,0), "mod_assets/images/alice/deformy.png")
image alice 3st = im.Composite((960,960), (0,0), "mod_assets/images/alice/2l.png", (0,0), "mod_assets/images/alice/1r.png", (0,0), "mod_assets/images/alice/t.png", (0,0), "mod_assets/images/alice/deformy.png")
image alice 3su = im.Composite((960,960), (0,0), "mod_assets/images/alice/2l.png", (0,0), "mod_assets/images/alice/1r.png", (0,0), "mod_assets/images/alice/u.png", (0,0), "mod_assets/images/alice/deformy.png")



image alice 3y1 = im.Composite((960,960), (0,0), "mod_assets/images/alice/2l.png", (0,0), "mod_assets/images/alice/1r.png", (0,0), "mod_assets/images/alice/y1.png")
image alice 3y2 = im.Composite((960,960), (0,0), "mod_assets/images/alice/2l.png", (0,0), "mod_assets/images/alice/1r.png", (0,0), "mod_assets/images/alice/y2.png")
image alice 3y3 = im.Composite((960,960), (0,0), "mod_assets/images/alice/2l.png", (0,0), "mod_assets/images/alice/1r.png", (0,0), "mod_assets/images/alice/y3.png")
image alice 3y4 = im.Composite((960,960), (0,0), "mod_assets/images/alice/2l.png", (0,0), "mod_assets/images/alice/1r.png", (0,0), "mod_assets/images/alice/y4.png")
image alice 3y5 = im.Composite((960,960), (0,0), "mod_assets/images/alice/2l.png", (0,0), "mod_assets/images/alice/1r.png", (0,0), "mod_assets/images/alice/y5.png")


image alice 3sy1 = im.Composite((960,960), (0,0), "mod_assets/images/alice/2l.png", (0,0), "mod_assets/images/alice/1r.png", (0,0), "mod_assets/images/alice/y1.png", (0,0), "mod_assets/images/alice/deformy.png")
image alice 3sy2 = im.Composite((960,960), (0,0), "mod_assets/images/alice/2l.png", (0,0), "mod_assets/images/alice/1r.png", (0,0), "mod_assets/images/alice/y2.png", (0,0), "mod_assets/images/alice/deformy.png")
image alice 3sy3 = im.Composite((960,960), (0,0), "mod_assets/images/alice/2l.png", (0,0), "mod_assets/images/alice/1r.png", (0,0), "mod_assets/images/alice/y3.png", (0,0), "mod_assets/images/alice/deformy.png")
image alice 3sy4 = im.Composite((960,960), (0,0), "mod_assets/images/alice/2l.png", (0,0), "mod_assets/images/alice/1r.png", (0,0), "mod_assets/images/alice/y4.png", (0,0), "mod_assets/images/alice/deformy.png")
image alice 3sy5 = im.Composite((960,960), (0,0), "mod_assets/images/alice/2l.png", (0,0), "mod_assets/images/alice/1r.png", (0,0), "mod_assets/images/alice/y5.png", (0,0), "mod_assets/images/alice/deformy.png")






image alice 4a = im.Composite((960,960), (0,0), "mod_assets/images/alice/2l.png", (0,0), "mod_assets/images/alice/2r.png", (0,0), "mod_assets/images/alice/a.png")
image alice 4b = im.Composite((960,960), (0,0), "mod_assets/images/alice/2l.png", (0,0), "mod_assets/images/alice/2r.png", (0,0), "mod_assets/images/alice/b.png")
image alice 4c = im.Composite((960,960), (0,0), "mod_assets/images/alice/2l.png", (0,0), "mod_assets/images/alice/2r.png", (0,0), "mod_assets/images/alice/c.png")
image alice 4d = im.Composite((960,960), (0,0), "mod_assets/images/alice/2l.png", (0,0), "mod_assets/images/alice/2r.png", (0,0), "mod_assets/images/alice/d.png")
image alice 4e = im.Composite((960,960), (0,0), "mod_assets/images/alice/2l.png", (0,0), "mod_assets/images/alice/2r.png", (0,0), "mod_assets/images/alice/e.png")
image alice 4f = im.Composite((960,960), (0,0), "mod_assets/images/alice/2l.png", (0,0), "mod_assets/images/alice/2r.png", (0,0), "mod_assets/images/alice/f.png")
image alice 4g = im.Composite((960,960), (0,0), "mod_assets/images/alice/2l.png", (0,0), "mod_assets/images/alice/2r.png", (0,0), "mod_assets/images/alice/g.png")
image alice 4h = im.Composite((960,960), (0,0), "mod_assets/images/alice/2l.png", (0,0), "mod_assets/images/alice/2r.png", (0,0), "mod_assets/images/alice/h.png")
image alice 4i = im.Composite((960,960), (0,0), "mod_assets/images/alice/2l.png", (0,0), "mod_assets/images/alice/2r.png", (0,0), "mod_assets/images/alice/i.png")
image alice 4j = im.Composite((960,960), (0,0), "mod_assets/images/alice/2l.png", (0,0), "mod_assets/images/alice/2r.png", (0,0), "mod_assets/images/alice/j.png")
image alice 4k = im.Composite((960,960), (0,0), "mod_assets/images/alice/2l.png", (0,0), "mod_assets/images/alice/2r.png", (0,0), "mod_assets/images/alice/k.png")
image alice 4l = im.Composite((960,960), (0,0), "mod_assets/images/alice/2l.png", (0,0), "mod_assets/images/alice/2r.png", (0,0), "mod_assets/images/alice/l.png")
image alice 4m = im.Composite((960,960), (0,0), "mod_assets/images/alice/2l.png", (0,0), "mod_assets/images/alice/2r.png", (0,0), "mod_assets/images/alice/m.png")
image alice 4n = im.Composite((960,960), (0,0), "mod_assets/images/alice/2l.png", (0,0), "mod_assets/images/alice/2r.png", (0,0), "mod_assets/images/alice/n.png")
image alice 4o = im.Composite((960,960), (0,0), "mod_assets/images/alice/2l.png", (0,0), "mod_assets/images/alice/2r.png", (0,0), "mod_assets/images/alice/o.png")
image alice 4p = im.Composite((960,960), (0,0), "mod_assets/images/alice/2l.png", (0,0), "mod_assets/images/alice/2r.png", (0,0), "mod_assets/images/alice/p.png")
image alice 4q = im.Composite((960,960), (0,0), "mod_assets/images/alice/2l.png", (0,0), "mod_assets/images/alice/2r.png", (0,0), "mod_assets/images/alice/q.png")
image alice 4r = im.Composite((960,960), (0,0), "mod_assets/images/alice/2l.png", (0,0), "mod_assets/images/alice/2r.png", (0,0), "mod_assets/images/alice/r.png")
image alice 4s = im.Composite((960,960), (0,0), "mod_assets/images/alice/2l.png", (0,0), "mod_assets/images/alice/2r.png", (0,0), "mod_assets/images/alice/s.png")
image alice 4t = im.Composite((960,960), (0,0), "mod_assets/images/alice/2l.png", (0,0), "mod_assets/images/alice/2r.png", (0,0), "mod_assets/images/alice/t.png")
image alice 4u = im.Composite((960,960), (0,0), "mod_assets/images/alice/2l.png", (0,0), "mod_assets/images/alice/2r.png", (0,0), "mod_assets/images/alice/u.png")


image alice 4sa = im.Composite((960,960), (0,0), "mod_assets/images/alice/2l.png", (0,0), "mod_assets/images/alice/2r.png", (0,0), "mod_assets/images/alice/a.png", (0,0), "mod_assets/images/alice/deform.png")
image alice 4sb = im.Composite((960,960), (0,0), "mod_assets/images/alice/2l.png", (0,0), "mod_assets/images/alice/2r.png", (0,0), "mod_assets/images/alice/b.png", (0,0), "mod_assets/images/alice/deform.png")
image alice 4sc = im.Composite((960,960), (0,0), "mod_assets/images/alice/2l.png", (0,0), "mod_assets/images/alice/2r.png", (0,0), "mod_assets/images/alice/c.png", (0,0), "mod_assets/images/alice/deform.png")
image alice 4sd = im.Composite((960,960), (0,0), "mod_assets/images/alice/2l.png", (0,0), "mod_assets/images/alice/2r.png", (0,0), "mod_assets/images/alice/d.png", (0,0), "mod_assets/images/alice/deform.png")
image alice 4se = im.Composite((960,960), (0,0), "mod_assets/images/alice/2l.png", (0,0), "mod_assets/images/alice/2r.png", (0,0), "mod_assets/images/alice/e.png", (0,0), "mod_assets/images/alice/deform.png")
image alice 4sf = im.Composite((960,960), (0,0), "mod_assets/images/alice/2l.png", (0,0), "mod_assets/images/alice/2r.png", (0,0), "mod_assets/images/alice/f.png", (0,0), "mod_assets/images/alice/deform.png")
image alice 4sg = im.Composite((960,960), (0,0), "mod_assets/images/alice/2l.png", (0,0), "mod_assets/images/alice/2r.png", (0,0), "mod_assets/images/alice/g.png", (0,0), "mod_assets/images/alice/deform.png")
image alice 4sh = im.Composite((960,960), (0,0), "mod_assets/images/alice/2l.png", (0,0), "mod_assets/images/alice/2r.png", (0,0), "mod_assets/images/alice/h.png", (0,0), "mod_assets/images/alice/deform.png")
image alice 4si = im.Composite((960,960), (0,0), "mod_assets/images/alice/2l.png", (0,0), "mod_assets/images/alice/2r.png", (0,0), "mod_assets/images/alice/i.png", (0,0), "mod_assets/images/alice/deform.png")
image alice 4sj = im.Composite((960,960), (0,0), "mod_assets/images/alice/2l.png", (0,0), "mod_assets/images/alice/2r.png", (0,0), "mod_assets/images/alice/j.png", (0,0), "mod_assets/images/alice/deform.png")
image alice 4sk = im.Composite((960,960), (0,0), "mod_assets/images/alice/2l.png", (0,0), "mod_assets/images/alice/2r.png", (0,0), "mod_assets/images/alice/k.png", (0,0), "mod_assets/images/alice/deform.png")
image alice 4sl = im.Composite((960,960), (0,0), "mod_assets/images/alice/2l.png", (0,0), "mod_assets/images/alice/2r.png", (0,0), "mod_assets/images/alice/l.png", (0,0), "mod_assets/images/alice/deform.png")
image alice 4sm = im.Composite((960,960), (0,0), "mod_assets/images/alice/2l.png", (0,0), "mod_assets/images/alice/2r.png", (0,0), "mod_assets/images/alice/m.png", (0,0), "mod_assets/images/alice/deform.png")
image alice 4sn = im.Composite((960,960), (0,0), "mod_assets/images/alice/2l.png", (0,0), "mod_assets/images/alice/2r.png", (0,0), "mod_assets/images/alice/n.png", (0,0), "mod_assets/images/alice/deform.png")
image alice 4so = im.Composite((960,960), (0,0), "mod_assets/images/alice/2l.png", (0,0), "mod_assets/images/alice/2r.png", (0,0), "mod_assets/images/alice/o.png", (0,0), "mod_assets/images/alice/deform.png")
image alice 4sp = im.Composite((960,960), (0,0), "mod_assets/images/alice/2l.png", (0,0), "mod_assets/images/alice/2r.png", (0,0), "mod_assets/images/alice/p.png", (0,0), "mod_assets/images/alice/deform.png")
image alice 4sq = im.Composite((960,960), (0,0), "mod_assets/images/alice/2l.png", (0,0), "mod_assets/images/alice/2r.png", (0,0), "mod_assets/images/alice/q.png", (0,0), "mod_assets/images/alice/deformy.png")
image alice 4sr = im.Composite((960,960), (0,0), "mod_assets/images/alice/2l.png", (0,0), "mod_assets/images/alice/2r.png", (0,0), "mod_assets/images/alice/r.png", (0,0), "mod_assets/images/alice/deformy.png")
image alice 4ss = im.Composite((960,960), (0,0), "mod_assets/images/alice/2l.png", (0,0), "mod_assets/images/alice/2r.png", (0,0), "mod_assets/images/alice/s.png", (0,0), "mod_assets/images/alice/deformy.png")
image alice 4st = im.Composite((960,960), (0,0), "mod_assets/images/alice/2l.png", (0,0), "mod_assets/images/alice/2r.png", (0,0), "mod_assets/images/alice/t.png", (0,0), "mod_assets/images/alice/deformy.png")
image alice 4su = im.Composite((960,960), (0,0), "mod_assets/images/alice/2l.png", (0,0), "mod_assets/images/alice/2r.png", (0,0), "mod_assets/images/alice/u.png", (0,0), "mod_assets/images/alice/deformy.png")



image alice 4y1 = im.Composite((960,960), (0,0), "mod_assets/images/alice/2l.png", (0,0), "mod_assets/images/alice/2r.png", (0,0), "mod_assets/images/alice/y1.png")
image alice 4y2 = im.Composite((960,960), (0,0), "mod_assets/images/alice/2l.png", (0,0), "mod_assets/images/alice/2r.png", (0,0), "mod_assets/images/alice/y2.png")
image alice 4y3 = im.Composite((960,960), (0,0), "mod_assets/images/alice/2l.png", (0,0), "mod_assets/images/alice/2r.png", (0,0), "mod_assets/images/alice/y3.png")
image alice 4y4 = im.Composite((960,960), (0,0), "mod_assets/images/alice/2l.png", (0,0), "mod_assets/images/alice/2r.png", (0,0), "mod_assets/images/alice/y4.png")
image alice 4y5 = im.Composite((960,960), (0,0), "mod_assets/images/alice/2l.png", (0,0), "mod_assets/images/alice/2r.png", (0,0), "mod_assets/images/alice/y5.png")


image alice 4sy1 = im.Composite((960,960), (0,0), "mod_assets/images/alice/2l.png", (0,0), "mod_assets/images/alice/2r.png", (0,0), "mod_assets/images/alice/y1.png", (0,0), "mod_assets/images/alice/deformy.png")
image alice 4sy2 = im.Composite((960,960), (0,0), "mod_assets/images/alice/2l.png", (0,0), "mod_assets/images/alice/2r.png", (0,0), "mod_assets/images/alice/y2.png", (0,0), "mod_assets/images/alice/deformy.png")
image alice 4sy3 = im.Composite((960,960), (0,0), "mod_assets/images/alice/2l.png", (0,0), "mod_assets/images/alice/2r.png", (0,0), "mod_assets/images/alice/y3.png", (0,0), "mod_assets/images/alice/deformy.png")
image alice 4sy4 = im.Composite((960,960), (0,0), "mod_assets/images/alice/2l.png", (0,0), "mod_assets/images/alice/2r.png", (0,0), "mod_assets/images/alice/y4.png", (0,0), "mod_assets/images/alice/deformy.png")
image alice 4sy5 = im.Composite((960,960), (0,0), "mod_assets/images/alice/2l.png", (0,0), "mod_assets/images/alice/2r.png", (0,0), "mod_assets/images/alice/y5.png", (0,0), "mod_assets/images/alice/deformy.png")
