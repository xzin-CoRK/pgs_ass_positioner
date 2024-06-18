# Instructions

## Step 1 - Generate positional data XML from PGS subtitle file

Open your existing .PSG subtitle file in bdsup2sub, then export with the "XML/PNG" output format.

## Step 2 - Create ASS subtitle file

There's a few ways to handle this:
1) You can use Subtitle Edit to OCR your PGS subs (or your OCR program of choice), then save the resulting output in Advanced Substation Alpha (ASS) format.
2) Alternatively, you can use a web-sourced SRT file.  However, if you use this method, you must ensure that the SRT has the same number of elements as the PGS.

## Step 3 - Pre-style the ASS subtitle file

Open the .ASS file from step 2 in Subtitle Edit.  From the toolbar select File > Advanced Sub Station Alpha styles.  Set the following properties:
- Spacing: 0.0
- Angle 0.0
- Alignment: Left-aligned and vertically centered (first column, second row)
- Margins (left, right, vertical): 0

At this stage you can configure the font face, color, and font size however you wish.  To go the extra mile, you can open one of the subtitle images extracted in step 1 to get the hex color code of the original subtitles, then match that in your ASS styles settings.

Save the file.

## Step 4 - Run the script

Run the python script, being sure to modify the two path values such that they point at the extracted XML from step 1 and the ASS subtitle file from steps 2/3.

The script will be finished very quickly, and will output a new ASS file in the same director as your existing ASS file.

## Step 5 - Verify and tweak

Open your ASS file in Subtitle Edit and load your video into the video preview.  Verify that the positioning looks good.  The script has an `x_offset` and `y_offset` value that can be used to shift all subtitle positions by a set amount -- depending on the font you've selected, this might help dial in the perfect placement.
