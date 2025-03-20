# Antenna

I tried adding an antenna to one of the RPi ZeroW boards.
First attempt was ugly, probably broke or fried something.
Second attempt was better, but I did correct a bridged gap, so I'm willing to concede a fried board.
It boots, but it says network is unreachable.

`ifconfig` on the bad board just shows the loopback interface.
`ifconfig` on a good board shows loopback and wlan0.

`ifup` on a good board exits 0
`/etc/networking/interfaces.d/` is empty on a bad and on a good board

Should I attempt the antenna on the good board?
I need to install the good board into the pager regardless, so do that first.
In the meantime, I'd rather be working on tenet...
