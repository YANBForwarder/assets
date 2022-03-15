# YANBF Custom Banners / Sounds repository.

A community provided repository of custom banners/sounds to enhance your YANBF forwarders!

## Want to make your own?
A quick tutorial to make one is here (thanks to Yrouel on GBAtemp!): https://gbatemp.net/threads/simple-tutorial-rescaling-resizing-images-to-use-as-3ds-banner-with-yanbf-using-lunapic-com-free-online-image-editor.609242/

Technical definitions (for those who know their stuff):
- Image must be in PNG format. It must be 256x128. You can center your image accordingly, but the resulting file _must_ be that size or it will fail to generate.
- Sound must be in WAV format, 16-bit, and shorter than 3 seconds. Otherwise, the 3DS will fail to render the banner entirely.

## Contribution guidelines
Any contribution is accepted, provided that you acknowledge that all provided assets will be under the CC0-1.0 license. See [license_assets.txt](https://github.com/lifehackerhansol/YANBF-assets/blob/main/license_assets.txt), or see https://creativecommons.org/publicdomain/zero/1.0/ for details.

1. Confirm it actually works. Test it on your own console.
1. Learn how to use git locally. GitHub Desktop works if you wish.
1. In the `assets` folder, create a directory with the name being your game's gamecode, in all caps. 
    - You can find this gamecode on your cartridge (i.e. in `NTR-IPKE-USA`, `IPKE` is your gamecode.) You can also use [NDSHeader](https://projectpokemon.org/home/files/file/2122-ndsheader/), a hex editor, or view it in TWiLight Menu++, etc.
    - If this game is multi region, consider using only the first three letters of the gamecode. This will make your submission usable on all regions. If a new region (say, a Japanese version of the banner) is to be uploaded, they can specify the full gamecode, and it will use that, or default to the multi region version if it is not found.
1. **Mandatory:** Name your banner image `<gamecode>.png`. The image _must_ be in a PNG format.
1. **Optional:** Name your banner sound `<gamecode>.wav`. The sound _must_ be in WAV format. It should also be under 3 seconds, or the 3DS will fail to play it. Obviously test this stuff beforehand, as step 1 says.
1. Create a pull request here.
