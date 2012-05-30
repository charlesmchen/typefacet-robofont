TypeFacet-RoboFont
===============================

A collection of free and open-source robofont extensions and scripts.

Distributed as the TypeFacet-RoboFont extension


Scripts
-------

### RFMergePointsNotUpdatingControlPoints
### RFMergePointsUpdatingControlPoints

Scripts that merge the selected points in the current glyph into a single point.

 * Only straight segment and bezier curve end points can be selected as inputs, not bezier control points.
 * The "UpdatingControlPoints" version also updates adjacent control points.
 

### RFCleanupSelectedGlyphContours
### RFCleanupAllGlyphContours

Scripts that clean up glyph contours.
 
 * Removes straight segments within contours that have the same start point and end point.
 * Converts bezier curves to straight segments if their control points are the same as their endpoints (a trivial case of straightness).
 
#### TODO

This script could do a lot more.

 * It could convert all straight curves to straight segments (not just the trivial case).
 * It could remove empty bezier curves, not just empty straight segments.
 
Also, it'd be nice to add a progress bar as it is fairly slow.

### RFAlignGlyph

Palette to facilitate re-aligning entire glyphs.

### RFSelectEntireContours

Selects all points in a contour if any point in that contour is selected.

### RFAlignAllTangents
### RFAlignAllTangentsCurvify
### RFAlignSelectedTangents
### RFAlignSelectedTangentsCurvify

Aligns tangents so that incoming and outgoing tangents of points are parallel.

 * The "Selected" versions only updates selected endpoints.
 * The "Curvify" versions convert straight segments to cubic bezier curves.


How To Install
--------------

 * Download distribution
 
 https://github.com/charlesmchen/typefacet-robofont/zipball/master
 
 * Unzip 
 * Double-Click the "TypeFacet-RoboFont.roboFontExt" file in the "extension" folder.
 
 
License 
-------

Available under the Apache Software License 2.0

