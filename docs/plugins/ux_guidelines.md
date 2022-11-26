# User Experience Guidelines

## Related information

- [CZI workshop](https://chanzuckerberg.github.io/napari-plugin-accel-workshops/workshops/february.html)
Related [workshop Lia slides](https://docs.google.com/presentation/d/10pxnwvBBb1rYV-LEWgmn5b2n9CK93-Qc_U_CEKUD5jI/edit#slide=id.g1197662a91c_0_66) and [isabela slides](https://docs.google.com/presentation/d/1JeDCvSYxXXDBMGdtC32rQSi5TJawiZEFW-A1wqHRHhU/edit#slide=id.g11d41ea185c_0_459).


## Layout

- Overview of UX
- Consitency with napari
- Menus and tooltips
- Containers and tabs

## Guiding principles

- Minimise popups
- Minimise the use of extra windows.


## Overview of UX

Briefly, accounting for user experience (UX) is accounting for how user interacts with your napari package.
It is important to keep in mind that what you have designed for is not necessarily how users will try to interact with your package.
Achieving a good user experience will facilatate ease of use of your package and user efficiency, improving the overall perception of your package.
This page includes some overall considerations related to achieving a smooth UX in addtion to specific napari tips.

## Design considerations

Keeping the UX in mind throughout the software design process is very valuable, but it is never too late to start.
Some important design considerations are:

1. **Who** is your target user?
2. **What** problems are you solving or enabling the user to do, what is the user outcome?
3. **Wow** this solution is unique and impactful to your users, what sets your package apart from other similar packages?

### Getting feedback

Some questions to ask yourself are:

- Where might users get confused or break something?
- Does our plugin description or tutorial include all necessary information?
- Have we chosen the best GUI to help users best understand the plugin functionality?
- What other use cases might our plugin have?

- Assess the user journey in using your package to overcome these challenges.
- What sets your package apart, why use it over other options to solve those challenges.
- Show your package to potential users and iterate with their feedback.

## Widget design considerations

TODO in progress with examples for the below.

A well designed widget enables your users to take full advantage of your widget functionality.

### Group similar actions together in your widget
Following the [Gestalt principles](https://www.toptal.com/designers/ui/gestalt-principles-of-design#:~:text=There%20are%20six%20individual%20principles,order%20(also%20called%20pr%C3%A4gnanz).), we naturally perceive nearby objects to be similar.
As such, grouping similar actions together enables a natural interation.
Containers and tabs can used to further group actions together and lessen clutter.
TODO example in progress.

Keep in mind that the napari viewer is configurable. Users can float (or popout) your widget windows, move them around, organise them into containers with tabs etc. So try to keep pieces of functionality well grouped together.

### Add tooltips

Adding tooltips to explain paramters allows users to find the information if they need it, but it won't take up unnecessary space.
TODO example with magicgui and QWdiget ready.

### Magicgui

There are standarised options (kind of) for different input styles, and using magicgui can make this process much simpler.

## NB I think there is a push towards supporting more with plugins

When that happens, I think this could be a very valuable space to desribe the UI sections (menu bar, layers, console etc.) - and what we might expect could modify each of these. Some does and don'ts style tips.

When the command palette is added the list expands etc.

### Preferences

Some information about napari preferences.