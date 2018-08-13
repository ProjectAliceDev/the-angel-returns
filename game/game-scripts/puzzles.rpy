label ch0_puzzle:
    if persistent.ctf_mode == True:
        call ctf_intro
    else:
        call ch0_blackbox_puzzle
    return

label ch1_puzzle:
    if persistent.ctf_mode == True:
        call ctf_cipher
        pass
    else:
        call ch1_blackbox_puzzle
    return