# Development journey: from a private study board to a public, IP-clean repo

Nov 14, 2026

## Summary

These notes started as a private whiteboard for learning Dan Kieft's AI cartoon-show workflow from his video and prompt page, written for a reader with no animation background. The private board quoted all 18 of his prompts word for word and showed his own pictures and story. This public version follows the same playbook as [ai-commercial-workflow-guide](https://github.com/az9713/ai-commercial-workflow-guide/blob/main/docs/DEVELOPMENT_JOURNEY.md), [cinematic-ai-ad-workflow-guide](https://github.com/az9713/cinematic-ai-ad-workflow-guide/blob/main/docs/DEVELOPMENT_JOURNEY.md) and [ai-animation-workflow-guide](https://github.com/az9713/ai-animation-workflow-guide/blob/main/docs/DEVELOPMENT_JOURNEY.md): keep our own commentary, drop everything copied, and replace the worked example with an original one generated on fal.

|  | Private study board | Public repo |
| --- | --- | --- |
| Worked example | The creator's own sketch: his story, his cartoon self, his robot, his sets | *Spare Specs*: our story, our characters (Marta the lighthouse keeper, Gus the gull), our sets |
| Prompts | All 18 of the creator's prompts, verbatim | None of his; our own 21 prompts instead, in `docs/PROMPTS.md` |
| Images | 13 pictures from his prompt page | 21 originals generated on fal (12 colour assets, 8 storyboard panels, 1 flawed first try kept as a lesson) |
| Board text | Summaries with his one-line examples, character names and dialogue | Same summaries; examples rewritten in our own words; his names and dialogue removed |
| Storyboard | None | New Round 5: an 8-panel pencil storyboard of our story |

## Decisions

| Question | Choice |
| --- | --- |
| Creator's name and links | Kept and credited: the notes are commentary on his tutorial |
| His style, characters, story | Not echoed. A deliberately different look (brush ink, gouache, printed-paper grain instead of a flat TV-sitcom look), a different cast and a different joke |
| Photo-to-cartoon steps | Shown with AI-generated "photos" (a gull, a lamp room) so no real photo of anyone is used |
| Model | FLUX.2 [klein] 9B on fal for everything: the cheapest model that was good enough for stylized stills, at 1024×576 |

## The fal pipeline

1. **Story first.** We wrote a short original sketch and an 8-shot list, then drew a pencil storyboard on fal to check the story read before spending on colour.
2. **Bases by text.** Style sheet, Marta's sheet, a gull photo, a lamp-room photo, the kitchen plate and the sea-chest sheet (6 text-to-image jobs).
3. **Everything else by editing.** Marta's outfit-only edit, the gull turned into a cartoon sheet, the photo turned into a set, the scene still built from four references, the close-up and the final wide. Editing from references keeps the cast consistent.
4. **Review every picture, and read them as a story.** Each image was checked in a browser. Fixes:
   - Storyboard: three panels redone (a split frame, a different face, glasses on the wrong character).
   - A continuity error caught by reading the panels in order: the glasses appeared on Gus only in panel 6. One-line edits put them on him in panels 4 and 5, which also made the joke stronger (dramatic irony).
   - Scene still: the first try put glasses on Marta and lit the lamp too early. One edit fixed both; the first try is kept in `images/` as a lesson.
5. **Collect.** The build workspace cannot reach `fal.media`, so each image was opened in a browser, checked, and captured at full size.
6. **Rebuild.** `whiteboard/board.json` written by script from the private board's structure with new text and image paths; `index.html` rebuilt with `tools/build.py`; tab renders re-shot with `tools/shot.py`; README regenerated with `tools/readme.py`; an overlap scan against the tutorial's transcript and prompt page found no shared run of 8 or more words outside titles and tool names.

Cost: 28 fal image jobs (7 text-to-image, 21 edits), about 17 cents at list price.

## Animation

7. **Three clips, not one.** The story was cut into three shots, each starting on an image we already had: the scene still (10 s, four lines), Gus's close-up (6 s, two lines, Marta off-screen) and the final wide (5 s, the payoff). Wan 3.0 Prime image-to-video on fal, 720p, audio on: the model generated both voices and the sound effects from the quoted lines and voice descriptions in each prompt.
8. **Check before stitching.** Contact sheets of every clip confirmed the continuity rules held (Gus keeps the glasses, Marta never has them, the lamp stays dark until the last shot), and a speech-to-text pass (fal Wizper) confirmed every line was spoken, in order, in the right clip.
9. **Stitch and publish.** ffmpeg joined the clips into one 21-second, 2.8 MB file; the README plays it inline.

Video cost: 21 seconds of Wan 3.0 Prime at 720p, $0.14 per second, $2.94 (clips: $1.40, $0.84, $0.70). Sound is not a separate charge: the model generates voices and effects in the same pass. Checking the dialogue with Wizper cost under a cent. Whole project: about $3.11 on fal. Note that Prime costs about 1.4x standard Wan 3.0; at 480p the same video would have been about $1.43.

## Lessons for next time

- Write the story and storyboard before any colour image: a continuity error costs a cent to fix in pencil and much more after animation.
- AI models drift in predictable ways (they add or move accessories, merge frames, change faces). Check each frame against the story, and fix with a small "change only X, keep everything else" edit instead of regenerating.
- A cheap distilled model is enough for teaching images; spend premium credits only where quality really matters.
