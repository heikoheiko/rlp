This code was originally developed here:
https://github.com/ethereum/pyethereum/blob/master/pyethereum/rlp.py

commit 8e0761a5fe94d2f8e7f8050e665e1a3c84e846b3
Author: Heiko Heiko <heiko@heiko.org>
Date:   Mon Dec 15 17:30:05 2014 +0100

    refactored to structlog

commit 45bf250664ca69bd643126f9957fa7f5a86be488
Author: Vitalik Buterin <v@buterin.com>
Date:   Mon Dec 15 06:10:48 2014 -0500

    Some modest optimizations

commit 6c414901f1ca7dbf8fb41c4fe68cec2b0ab65b2f
Merge: 9dcb2a3 a63372f
Author: Vitalik Buterin <v@buterin.com>
Date:   Wed Oct 1 15:24:29 2014 -0400

    merge

commit 094574109ed03451e884a5f02df54cc0f9a4faca
Author: maurycyp <github.com@wayheavy.com>
Date:   Wed Oct 1 12:30:08 2014 -0400

    Small fixes, cleanup, and PEP 8

commit a63372fb7a908fd9f7d9a4848b54cfdbe5c21773
Author: Heiko Heiko <heiko@heiko.org>
Date:   Wed Oct 1 18:06:48 2014 +0200

    catch deccoding error

commit 68c8f65659110c0e3e75edea5131a23d8c0b168d
Author: Vitalik Buterin <v@buterin.com>
Date:   Sun Aug 31 13:47:07 2014 -0400

    Modified the way storage is handled in the block-level cache

commit ddf8154b13c186388125366b0cf031a6ccd1cc17
Author: Vitalik Buterin <v@buterin.com>
Date:   Fri Aug 29 13:10:21 2014 -0400

    Made rlp decoding more strict

commit baff665aaf700b928e70c56a8e031a4e85821446
Author: Vitalik Buterin <v@buterin.com>
Date:   Mon Jul 21 08:17:19 2014 -0400

    Fixed rlp descend usage in block printing

commit b3925465a9abeb6684bcbf979bd59259c8e81604
Author: Chen Houwu <chenhouwu@gmail.com>
Date:   Fri May 30 00:29:36 2014 +0800

    update rlp description

commit c3a46900abd533e8720163825ddb3d22bc368c47
Author: Chen Houwu <chenhouwu@gmail.com>
Date:   Fri May 30 00:19:56 2014 +0800

    improve readability of rlp encoding

commit 368e0656c44cb4a65a02058a221fe913dafa66f4
Author: Vitalik Buterin <v@buterin.com>
Date:   Thu May 29 07:48:34 2014 -0400

    added rlp.concat

commit 7c6a437de14499cff570d65a138cace8776881fd
Author: Heiko Heiko <heiko@heiko.org>
Date:   Thu May 29 11:22:01 2014 +0200

    check pre-condition #84 #111

commit 53c0516f27ca24d4533d04bd2db2272446750cc6
Author: Heiko Heiko <heiko@heiko.org>
Date:   Fri May 2 12:15:23 2014 +0200

    fix: recursive imports

commit 481ae6c3f7fbece9f4d8a442032a5a99078446eb
Author: Vitalik Buterin <v@buterin.com>
Date:   Fri Apr 25 14:44:35 2014 -0400

    Added rlp.descend method for deserialization-free RLP access

commit ff8a2c7112cf0981b1e7555ba9bca3bf8b8c3004
Author: Chen Houwu <chenhouwu@gmail.com>
Date:   Fri Apr 4 13:11:23 2014 +0800

    remove relative import to enable running

commit 49eb48df18bb1f575fa429533f02719cc44cb2ac
Author: Chen Houwu <chenhouwu@gmail.com>
Date:   Tue Apr 1 14:42:33 2014 +0800

    use single code base for integer/big endian bin conversion

commit ff40ff3b0877263fb29dbc5f063260d20c9e097d
Merge: d92892a 36c3668
Author: Chen Houwu <chenhouwu@gmail.com>
Date:   Wed Mar 19 02:24:48 2014 +0800

    merge #24

commit 36c3668d9989ada69c26e3c6f965802f0e48720e
Author: Konrad Feldmeier <konrad.feldmeier@brainbot.com>
Date:   Tue Mar 18 12:30:28 2014 +0100

    Create package 'pyethereum'

    This moves all top-level modules into a package folder and
    also adjusts imports accordingly.
