# User Experience Guidelines

Accounting for user experience (UX) is handling how users interact with your napari package.
It is important to keep in mind that what you have designed for is not necessarily how users will try to interact with your package.
Achieving a good user experience will facilatate ease of use of your package and user efficiency, improving the overall perception of your package.
This page includes some overall considerations related to achieving a smooth UX in addtion to specific napari tips.

## Design considerations

Keeping the UX in mind throughout the software design process is very valuable, but it is never too late to start.
Some important design considerations are:

1. **Who** is your target user?
2. **What** problems are you solving or enabling the user to do, what is the user outcome?
3. **Wow** factor that makes your solution unique and impactful to your users, what sets your package apart from other similar packages?

### Questions to ask yourself

Some questions to ask yourself are:

- Where might users get confused or break something?
- Does our plugin description or tutorial include all necessary information?
- Have we chosen the best GUI to help users best understand the plugin functionality?
- What other use cases might our plugin have?

- Assess the user journey in using your package to overcome these challenges.
- What sets your package apart, why use it over other options to solve those challenges.
- Show your package to potential users and iterate with their feedback.

### Getting user feedback

CZI workshop

## Widget design considerations

A well designed widget enables your users to take full advantage of your widget functionality.
In addition to following the general design considerations above, there are specific considerations in creating a widget that can be helpful.

### Group similar actions together in your widget
Following the [Gestalt principles](https://www.toptal.com/designers/ui/gestalt-principles-of-design#:~:text=There%20are%20six%20individual%20principles,order%20(also%20called%20pr%C3%A4gnanz).), we naturally perceive nearby objects to be similar.
As such, grouping similar actions together enables a natural interation.
Containers and tabs can used to further group actions together and lessen clutter.
Keep in mind that the napari viewer is configurable. Users can float (or popout) your widget windows, move them around, organise them into containers with tabs etc. So try to keep pieces of functionality well grouped together.

### Add tooltips to widget items

Adding tooltips to explain paramters allows users to find the information if they need it, but it won't take up unnecessary space.
TODO

### Choose the correct UI element

Not sure on this one, but e.g. a check box for 2 or 3 items, radio button for multiple options (maybe max 4) and a drop down list otherwise.

## Related workshops

- [CZI workshop](https://chanzuckerberg.github.io/napari-plugin-accel-workshops/workshops/february.html)
Related [workshop Lia slides](https://docs.google.com/presentation/d/10pxnwvBBb1rYV-LEWgmn5b2n9CK93-Qc_U_CEKUD5jI/edit#slide=id.g1197662a91c_0_66) and [isabela slides](https://docs.google.com/presentation/d/1JeDCvSYxXXDBMGdtC32rQSi5TJawiZEFW-A1wqHRHhU/edit#slide=id.g11d41ea185c_0_459). example with magicgui and QWdiget ready.

<!-- ## Plugin modifiable sections

If UI elements become modifiable by plugins (e.g. layer list or bottom bar), this could be a space to desribe the UI sectionsand what we might expect could modify each of these.

If the command palette is added the list expands etc. -->