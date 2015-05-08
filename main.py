#!/usr/local/bin/python
__author__ = 'alexisgallepe'

import Torrent
import Tracker
import Peer
import struct
import PeersManager


if __name__ == '__main__':

    peers = []

    t = Torrent.Torrent("w.torrent")
    tk = Tracker.Tracker(t)

    peersLst = tk.getPeersFromTrackers()
    while peersLst.__sizeof__() == 0:
        print peersLst.__sizeof__()
        peersLst = tk.getPeersFromTrackers()

    peersLst = peersLst[:8]
    print "get peers from tracker"

    for peer in peersLst:
        p = Peer.Peer(t)
        if p.connectToPeer(peer):
            peers.append(p)

    p = PeersManager.PeerManager(peers,t)
    p.start()

    for p in peers:
        p.sendToPeer(p.handshake)
        interested = struct.pack('!I', 1) + struct.pack('!B', 2)
        p.sendToPeer(interested)
        print "handshake sent"


