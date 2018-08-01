#GOBFADU Policy 1.8 DDLC Edition 6/15/2018
#Python 3.8 MOS Edition 6/12/2018

label gobfadupolicytests:
    stop music fadeout 2.0
#    scene black
#    with dissolve_scene_full
    call gobfadutestverify
label gobfadutestverify:
    if renpy.exists("../game/GOBFADUTestLock.rpyc"):
        pass
    else:
        call screen dialog(message="GOBFADU Assets Missing. Please reinstall the Operating System.", ok_action=Function(renpy.quit))
