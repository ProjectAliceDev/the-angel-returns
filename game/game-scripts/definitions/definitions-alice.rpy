## Alice Angel
## Note: The '0' indicates the original sprite modifications as by BippityZop.
## The 'b' in front of '0' will indicate whether she is disfigured or not.
## Any other integer indicates sprites made by yagamirai10.
image alice mesh = "mod_assets/images/alice/mesh.png"
image alice 0a = "mod_assets/images/alice/a.png"
image alice 0b = "mod_assets/images/alice/b.png"
image alice 0c = "mod_assets/images/alice/c.png"
image alice 0d = "mod_assets/images/alice/d.png"
image alice 0e = "mod_assets/images/alice/e.png"
image alice 0f = "mod_assets/images/alice/f.png"
image alice 0g = "mod_assets/images/alice/g.png"
image alice 0h = "mod_assets/images/alice/h.png"
image alice 0i = "mod_assets/images/alice/i.png"
image alice 0j = "mod_assets/images/alice/j.png"
image alice 0k = "mod_assets/images/alice/k.png"
image alice 0l = "mod_assets/images/alice/l.png"
image alice 0m = "mod_assets/images/alice/m.png"
image alice 0n = "mod_assets/images/alice/n.png"
image alice 0o = "mod_assets/images/alice/o.png"
image alice 0p = "mod_assets/images/alice/p.png"
image alice 0q = "mod_assets/images/alice/q.png"
image alice 0r = "mod_assets/images/alice/r.png"
image alice 0s = "mod_assets/images/alice/s.png"
image alice 0t = "mod_assets/images/alice/t.png"
image alice 0u = "mod_assets/images/alice/u.png"

image alice 0ba = im.Composite((960,960), (0,0), "mod_assets/images/alice/a.png", (0,0), "mod_assets/images/alice/susie.png")
image alice 0bb = im.Composite((960,960), (0,0), "mod_assets/images/alice/b.png", (0,0), "mod_assets/images/alice/susie.png")
image alice 0bc = im.Composite((960,960), (0,0), "mod_assets/images/alice/c.png", (0,0), "mod_assets/images/alice/susie.png")
image alice 0bd = im.Composite((960,960), (0,0), "mod_assets/images/alice/d.png", (0,0), "mod_assets/images/alice/susie.png")
image alice 0be = im.Composite((960,960), (0,0), "mod_assets/images/alice/e.png", (0,0), "mod_assets/images/alice/susie.png")
image alice 0bf = im.Composite((960,960), (0,0), "mod_assets/images/alice/f.png", (0,0), "mod_assets/images/alice/susie.png")
image alice 0bg = im.Composite((960,960), (0,0), "mod_assets/images/alice/g.png", (0,0), "mod_assets/images/alice/susie.png")
image alice 0bh = im.Composite((960,960), (0,0), "mod_assets/images/alice/h.png", (0,0), "mod_assets/images/alice/susie.png")
image alice 0bi = im.Composite((960,960), (0,0), "mod_assets/images/alice/i.png", (0,0), "mod_assets/images/alice/susie.png")
image alice 0bj = im.Composite((960,960), (0,0), "mod_assets/images/alice/j.png", (0,0), "mod_assets/images/alice/susie.png")
image alice 0bk = im.Composite((960,960), (0,0), "mod_assets/images/alice/k.png", (0,0), "mod_assets/images/alice/susie.png")
image alice 0bl = im.Composite((960,960), (0,0), "mod_assets/images/alice/l.png", (0,0), "mod_assets/images/alice/susie.png")
image alice 0bm = im.Composite((960,960), (0,0), "mod_assets/images/alice/m.png", (0,0), "mod_assets/images/alice/susie.png")
image alice 0bn = im.Composite((960,960), (0,0), "mod_assets/images/alice/n.png", (0,0), "mod_assets/images/alice/susie.png")
image alice 0bo = im.Composite((960,960), (0,0), "mod_assets/images/alice/o.png", (0,0), "mod_assets/images/alice/susie.png")
image alice 0bp = im.Composite((960,960), (0,0), "mod_assets/images/alice/p.png", (0,0), "mod_assets/images/alice/susie.png")
image alice 0bq = im.Composite((960,960), (0,0), "mod_assets/images/alice/q.png", (0,0), "mod_assets/images/alice/susie.png")
image alice 0br = im.Composite((960,960), (0,0), "mod_assets/images/alice/r.png", (0,0), "mod_assets/images/alice/susie.png")
image alice 0bs = im.Composite((960,960), (0,0), "mod_assets/images/alice/s.png", (0,0), "mod_assets/images/alice/susie.png")
image alice 0bt = im.Composite((960,960), (0,0), "mod_assets/images/alice/t.png", (0,0), "mod_assets/images/alice/susie.png")
image alice 0bu = im.Composite((960,960), (0,0), "mod_assets/images/alice/u.png", (0,0), "mod_assets/images/alice/susie.png")


image alice eyes = LiveComposite((1280, 720), (0, 0), "mod_assets/images/alice/eyes1.png", (0, 0), "alicepupils")

image alice eyes_base = "mod_assets/images/alice/eyes1.png"

image alicepupils:
    "mod_assets/images/alice/eyes2.png"
    yuripupils_move

image alice glitch:
    block:
        choice:
            "mod_assets/images/alice/glitch1.png"
        choice:
            "mod_assets/images/alice/glitch2.png"
        choice:
            "mod_assets/images/alice/glitch3.png"
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