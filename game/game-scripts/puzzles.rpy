label ch0_puzzle:
    if persistent.ctf_mode == True:
        call intro_ctf
    else:
        call ch0_blackbox_puzzle
    return

label ch1_puzzle:
    if persistent.ctf_mode == True:
        # call mail_ctf
        pass
    else:
        call ch1_blackbox_puzzle
    return