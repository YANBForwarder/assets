# YANBF Custom Banners / Sounds repository.

A community provided repository of custom banners/sounds to enhance your YANBF forwarders!

## Want to make your own?
A quick tutorial to make one is here (thanks to Yrouel on GBAtemp!): https://gbatemp.net/threads/simple-tutorial-rescaling-resizing-images-to-use-as-3ds-banner-with-yanbf-using-lunapic-com-free-online-image-editor.609242/

Technical definitions (for those who know their stuff):
- Image must be in PNG format. It must be 256x128. You can center your image accordingly, but the resulting file _must_ be that size or it will fail to generate.
- Sound must be in WAV format, 16-bit, and shorter than 3 seconds. Otherwise, the 3DS will fail to render the banner entirely. Your sound will also fail if it is in mono, though your banner will still render, so make sure you use stereo tracks for your WAV.

## Contribution guidelines
Any contribution is accepted, provided that you acknowledge that all provided assets will be under the CC0-1.0 license. See [license_assets.txt](https://github.com/lifehackerhansol/YANBF-assets/blob/main/license_assets.txt), or see https://creativecommons.org/publicdomain/zero/1.0/ for details.

1. Confirm it actually works. Test it on your own console.
1. Learn how to use git locally. GitHub Desktop works if you wish.
1. In the `assets` folder, create a directory with the name being your game's gamecode, in all caps. 
    - You can find this gamecode on your cartridge (i.e. in `NTR-IPKE-USA`, `IPKE` is your gamecode.) You can also use [NDSHeader], a hex editor, or view it in TWiLight Menu++, etc.
    - If this game is multi region, consider using only the first three letters of the gamecode. This will make your submission usable on all regions. If a new region (say, a Japanese version of the banner) is to be uploaded, they can specify the full gamecode, and it will use that, or default to the multi region version if it is not found.
1. **Mandatory:** Name your banner image `<gamecode>.png`. The image _must_ be in a PNG format.
1. **Optional:** Name your banner sound `<gamecode>.wav`. The sound _must_ be in 16 bit PCM WAV format. It should also be under 3 seconds, or the 3DS will fail to play it. Obviously test this stuff beforehand, as step 1 says.
1. Create a pull request here.

## Useful tools
- [YANBForwarder Assets thread on GBATemp](https://gbatemp.net/threads/yanbf-custom-banner-and-sound-requests.611460/)
- [YANBForwarder thread on GBATemp](https://gbatemp.net/threads/nds-yet-another-nds-bootstrap-forwarder-more-than-40-forwarders-are-now-possible.606138/) and [YANBForwarder GitHub](https://github.com/YANBForwarder/YANBF)
- [khinsider.com](https://downloads.khinsider.com/): want a specific sound effect or OST from the NDS game? Someone's probably already ripped it and uploaded it here.
- [LunaPic](https://www9.lunapic.com/editor/) free online photo editor
- [VGMTrans](https://github.com/vgmtrans/vgmtrans/): can rip sound effects and OST from NDS cartridge dumps (they must still be converted to WAV)
- [Audacity](https://github.com/audacity/audacity/releases/tag/Audacity-3.0.2) (v3.0.2 is the last confirmed no-telemetry build, after all the controversy) can trim and convert sound for you.
- [HXD Hex Editor](https://mh-nexus.de/en/hxd/), useful for checking for gamecodes at the beginning of NDS cartridge dumps; [NDSHeader] is easier and more foolproof

[NDSHeader]: https://projectpokemon.org/home/files/file/2122-ndsheader/
