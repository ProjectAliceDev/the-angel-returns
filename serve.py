## Python Serve Script
import os
get_time = "something"
with open("version.py", 'w+') as st:
    st.write("init python:")
    st.write("    snapshottime = " + get_time)
os.system("./renpy.sh "../mod/" lint && ./renpy.sh launcher distribute "../mod/" && cd ..")
