# Our prompts for *Spare Specs*

Every image in `images/` and the exact prompt that made it, in the order they were made. All were run on [fal](https://fal.ai) with FLUX.2 [klein] 9B (`fal-ai/flux-2/klein/9b` for text-to-image, `.../edit` when reference images are passed), at 1024×576, 8 steps. "image 1, image 2" in a prompt means the first and second reference images listed under *References*.

These are original prompts written for this repo. They follow the structure the tutorial teaches (references, subject, layout, a style block reused word for word, exclusions) but none of its text.

## `images/style-sheet.jpg`: Style reference sheet

- Model: `fal-ai/flux-2/klein/9b`
- References: text only

> A cartoon style reference sheet on cream paper, no text: a row of six round paint swatches in sea green, cream, coral, navy, mustard and warm grey; below them sample brush strokes in thick black ink that swell and taper; below that a small teapot, a rowboat and a rubber boot drawn in the style: bold black brush-ink outlines of varying thickness, chunky rounded shapes, flat gouache colour fills with visible brush texture, printed on rough uncoated paper with faint paper grain and slightly offset colour.

## `images/marta-sheet.jpg`: Marta: character sheet

- Model: `fal-ai/flux-2/klein/9b`
- References: text only

> Cartoon character turnaround sheet of an original character: a stout, cheerful elderly lighthouse keeper woman with a grey hair bun, round wire glasses, rosy cheeks, navy cable-knit jumper, yellow oilskin trousers and black rubber boots. Front view, three-quarter view and side view of the same woman standing side by side at identical size, neutral pose, on a plain cream background, no text. Storybook cartoon style: bold black brush-ink outlines that thicken and thin, chunky rounded shapes, small round bead eyes with one white highlight, flat gouache colours with visible brush texture, limited palette of sea green, cream, coral and navy, faint paper grain.

## `images/marta-sunday.jpg`: Marta: outfit-only edit

- Model: `fal-ai/flux-2/klein/9b/edit`
- References: image 1 = Marta's sheet

> The same turnaround sheet of the same woman as image 1, same three views, same pose, size, face, hair bun, glasses, line style and cream background. Only the outfit changes: a coral knitted cardigan over a cream blouse, a navy skirt with small white flowers, thick grey socks and brown lace-up shoes. No text.

## `images/gus-photo.jpg`: Gus: reference photo

- Model: `fal-ai/flux-2/klein/9b`
- References: text only

> Wildlife photograph of a herring gull standing on a weathered wooden harbour post, full body side view, white head, grey wings with black wingtips, yellow beak with a red spot, pink legs, overcast soft light, shallow depth of field, grey sea in the background.

## `images/gus-sheet.jpg`: Gus: photo to cartoon sheet

- Model: `fal-ai/flux-2/klein/9b/edit`
- References: image 1 = gull photo, image 2 = Marta's sheet (style)

> Turn the gull in image 1 into a cartoon character turnaround sheet, drawn in the style of image 2: front view, three-quarter view and side view of the same chubby herring gull standing side by side at identical size on a plain cream background, no text. Keep its markings: white head and body, grey wings with black tips, yellow beak with a red spot, pink legs. Bold black brush-ink outlines that thicken and thin, chunky rounded shapes, small round bead eyes with one white highlight, flat gouache colour with visible brush texture, faint paper grain.

## `images/lamproom-photo.jpg`: Lamp room: reference photo

- Model: `fal-ai/flux-2/klein/9b`
- References: text only

> Interior photograph of the lamp room at the top of an old lighthouse: a large glass Fresnel lens with brass frame in the centre, curved windows all around looking out to a calm grey sea, a narrow iron walkway with a railing, white painted metal walls, a small wooden stool, daylight, empty, no people, realistic photo.

## `images/lamproom-plate.jpg`: Lamp room: photo to background plate

- Model: `fal-ai/flux-2/klein/9b/edit`
- References: image 1 = lamp-room photo, image 2 = kitchen plate (style)

> Redraw the lighthouse lamp room photo in image 1 as an empty cartoon background, keeping its layout: the big lens in the centre, the curved windows, the railing and the stool. Draw it in the style of image 2: bold black brush-ink outlines that thicken and thin, chunky rounded shapes, flat gouache colours with visible brush texture, palette of sea green, cream, coral and navy, faint paper grain. Dusk light. Leave open floor space in the front for characters. No characters, no text.

## `images/kitchen-plate.jpg`: Kitchen: background plate from text

- Model: `fal-ai/flux-2/klein/9b`
- References: text only

> Empty cartoon background of a lighthouse keeper's cottage kitchen, wide shot at eye level: a sea-green iron stove on the left, a round porthole window in the centre showing the sea, a wooden table with a teapot, shelves of tins and jars, a coat hook with a yellow oilskin, black and cream checkered floor with open space in the front for characters. No characters, no text. Storybook cartoon style: bold black brush-ink outlines that thicken and thin, chunky rounded shapes, flat gouache colours with visible brush texture, palette of sea green, cream, coral and navy, faint paper grain.

## `images/chest-sheet.jpg`: Sea chest: prop sheet

- Model: `fal-ai/flux-2/klein/9b`
- References: text only

> Cartoon prop reference sheet: an old wooden sea chest with brass corners and a rope handle, lid open, a coil of rope, a rolled sea chart and a brass spyglass poking out. Front view and three-quarter view of the same chest side by side at identical size on a plain cream background, no text, no characters. Storybook cartoon style: bold black brush-ink outlines that thicken and thin, chunky rounded shapes, flat gouache colours with visible brush texture, faint paper grain.

## `images/scene-still-first-try.jpg`: Scene still (first try)

- Model: `fal-ai/flux-2/klein/9b/edit`
- References: image 1 = Marta, 2 = Gus, 3 = lamp-room plate, 4 = sea chest

> One single cartoon scene, wide shot at eye level, inside the lighthouse lamp room from image 3 at dusk, same style, colours and layout. On the left, the woman from image 1, same face, bun, navy jumper, yellow trousers and boots but NOT wearing glasses, kneels at the open sea chest from image 4 and digs through the rope, squinting. On the right, the gull from image 2 stands on the window rail, wearing small round wire glasses on its beak, looking innocently away. Characters drawn exactly in the style of images 1 and 2: bold black brush-ink outlines, flat gouache colours, faint paper grain. No text.

## `images/scene-still.jpg`: Scene still: the fix edit

- Model: `fal-ai/flux-2/klein/9b/edit`
- References: image 1 = the first try

> Remove the glasses from the kneeling grey-haired woman so her face and eyes are bare, squinting. Turn the lamp inside the big glass lens off, so it is dark and unlit. The gull on the right keeps its glasses. Keep everything else in the image exactly the same.

## `images/gus-closeup.jpg`: Clip 2 start frame: Gus close-up

- Model: `fal-ai/flux-2/klein/9b/edit`
- References: image 1 = Gus's sheet, image 2 = lamp-room plate

> Cartoon close-up of the gull from image 1, head and chest filling the frame, three-quarter view, wearing small round wire glasses on its beak, chest puffed out, looking smug, one eye half closed. Background: the sea-green window frame and a dusk sky from image 2, softly out of focus. Same style as image 1: bold black brush-ink outlines, flat gouache colours, faint paper grain. No text.

## `images/final-wide.jpg`: Final wide: the payoff

- Model: `fal-ai/flux-2/klein/9b/edit`
- References: image 1 = scene still

> The same lamp room, same style, same two characters as image 1, a moment later. The grey-haired woman, still with no glasses, has jumped up and lunges toward the right with both arms stretched out, open-mouthed. The gull with the round glasses hops sideways along the rail just out of her reach, wings half open, cheeky. Behind them the big lamp in the glass lens has switched on: it glows bright yellow and a wide beam of light shoots out of the window across the dusk sky. Rope from the sea chest spilled on the floor. Bold black brush-ink outlines, flat gouache colours, faint paper grain. No text.

## `images/sb01.jpg`: Storyboard 1

- Model: `fal-ai/flux-2/klein/9b`
- References: text only

> Rough pencil storyboard panel, grey graphite sketch on white paper with loose construction lines and light hatching, no colour, no text: extreme wide shot of a small white lighthouse on a rocky cliff above the sea at dusk, its lamp dark, a little cottage beside it, a few gulls in the sky.

## `images/sb02.jpg`: Storyboard 2

- Model: `fal-ai/flux-2/klein/9b/edit`
- References: image 1 = Marta's sheet

> Rough pencil storyboard panel, grey graphite sketch on white paper with loose construction lines and light hatching, no colour, no text. Medium shot inside a lighthouse lamp room: the stout elderly woman from image 1, with her grey bun, but WITHOUT glasses, squints at an open logbook held at arm's length, frowning. The big lens is behind her and windows show the sea.

## `images/sb03.jpg`: Storyboard 3

- Model: `fal-ai/flux-2/klein/9b/edit`
- References: image 1 = Marta's sheet, image 2 = sea chest

> Rough pencil storyboard panel, grey graphite sketch on white paper with loose construction lines, motion lines and light hatching, no colour, no text. The stout elderly woman from image 1, without glasses, kneels at the open wooden sea chest from image 2 and flings things over her shoulder: a coil of rope, a rolled chart and a spyglass flying through the air.

## `images/sb04.jpg`: Storyboard 4 (gull landing, then glasses added by edit)

- Model: `fal-ai/flux-2/klein/9b/edit`
- References: image 1 = gull photo; then image 1 = that panel, image 2 = panel 6

> Rough pencil storyboard panel, grey graphite sketch on white paper with loose construction lines, motion lines and light hatching, no colour, no text. A herring gull like the one in image 1 lands on the iron railing outside an open lighthouse window, wings spread wide, feet reaching for the rail, sea and sky behind.

> Fix: Put the small round wire glasses from image 2 on the gull in image 1, perched on its beak in front of its eyes. Keep everything else in the pencil sketch of image 1 exactly the same.

## `images/sb05.jpg`: Storyboard 5 (two-shot, two fix edits)

- Model: `fal-ai/flux-2/klein/9b/edit`
- References: image 1 = panel 3, image 2 = panel 4; then fixes

> One single rough pencil storyboard frame, grey graphite on white paper, light hatching, no colour, no text, no panel borders, not split. One continuous wide shot of one room, a round lighthouse lamp room with tall windows: at the left the elderly woman from image 1, bare-faced with no glasses on, kneels beside her open sea chest and looks up and to the right, hopeful; at the right, on the sill of an open window, the gull from image 2 stands with its head turned away from her, looking innocent.

> Fix 1: Remove the glasses from the kneeling woman's face so her eyes are bare. Keep everything else in the pencil sketch exactly the same.

> Fix 2: Edit only the gull's head: the gull on the window sill now wears one pair of small round wire glasses resting on its beak, like the gull in image 2. The gull keeps its wings folded and both feet on the sill, a normal bird with no hands. No other glasses anywhere. Keep the woman, the chest, the room and every other line of image 1 exactly the same.

## `images/sb06.jpg`: Storyboard 6

- Model: `fal-ai/flux-2/klein/9b/edit`
- References: image 1 = gull photo

> Rough pencil storyboard panel, grey graphite sketch on white paper with loose construction lines and light hatching, no colour, no text. Close-up of the head of a herring gull like the one in image 1, now wearing small round wire glasses perched on its beak, looking smug, chest puffed out.

## `images/sb07.jpg`: Storyboard 7

- Model: `fal-ai/flux-2/klein/9b/edit`
- References: image 1 = panel 3

> Rough pencil storyboard panel, grey graphite on white paper, light hatching, no colour, no text. Close-up of the same elderly woman as in image 1: same round soft face, same grey hair pulled into a bun, same cable-knit jumper, no glasses. She narrows her eyes in suspicion, one eyebrow raised, mouth pursed to one side. Cartoon proportions, friendly granny, not grotesque.

## `images/sb08.jpg`: Storyboard 8

- Model: `fal-ai/flux-2/klein/9b/edit`
- References: image 1 = panel 3, image 2 = panel 6

> Rough pencil storyboard panel, grey graphite on white paper, motion lines, light hatching, no colour, no text. Wide shot in a lighthouse lamp room. The elderly woman from image 1, bare-faced with NO glasses, lunges with both arms out. The gull from image 2, which IS wearing the small round glasses, hops along the window rail just out of her reach. Behind them the big lamp switches on and a bright beam shoots out of the window across the night sky.

## The reusable style block

This sentence (or a close variant) ends most colour prompts above. It plays the role of the STYLE block in the workflow: keep it identical and every asset looks like the same show.

> Storybook cartoon style: bold black brush-ink outlines that thicken and thin, chunky rounded shapes, small round bead eyes with one white highlight, flat gouache colours with visible brush texture, limited palette of sea green, cream, coral and navy, faint paper grain.
