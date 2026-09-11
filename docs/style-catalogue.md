# 16 style recipes

These are art-direction recipes, not sixteen automated scene converters. Design styles, lighting moods and presentation modes are explicitly distinguished. All numeric ranges are starting points, not material measurements. Physical displacement is total peak-to-peak relief in millimetres; use maps with calibrated neutral levels.

## Photoreal daylight · `photoreal-daylight`

**Type:** lighting. **Atmosphere:** neutral daylight.

- Palette: limestone, clear glass, neutral plaster.
- Roughness starting range: 0.45–0.8; exceptions such as glass use their own measured shader.
- Relief starting range: 0.1–0.6 mm.
- Light: Large sky fill plus one consistent sun; keep interiors readable without flattening contrast.
- Camera: Perspective, 28–50 mm full-frame equivalent; level verticals only when reference supports it.
- Finishing: Neutral WB; restrained highlight compression.
- Acceptance: Crisp contact shadows, plausible window reflections, no clipped white facade.
- Failure to avoid: Do not whiten every material or add a second contradictory sun.

**Image prompt starter:** Reinterpret the supplied architectural reference as photoreal daylight. Use limestone, clear glass, neutral plaster. Large sky fill plus one consistent sun; keep interiors readable without flattening contrast. Keep the building silhouette, window positions, perspective and image crop. Neutral WB; restrained highlight compression.

## Blue hour · `blue-hour`

**Type:** lighting. **Atmosphere:** cool dusk.

- Palette: cool concrete, warm timber, low-iron glass.
- Roughness starting range: 0.35–0.75; exceptions such as glass use their own measured shader.
- Relief starting range: 0.1–0.8 mm.
- Light: Cool sky plus 2700–3200 K luminaires, separated into interior/exterior groups.
- Camera: Lock reference pose; small exposure changes before changing lamp output.
- Finishing: Preserve blue exterior and warm interior separation; modest bloom.
- Acceptance: Visible fixtures retain shape; glass reveals depth and reflected sky.
- Failure to avoid: Do not compensate dark foliage with neon green albedo.

**Image prompt starter:** Reinterpret the supplied architectural reference as blue hour. Use cool concrete, warm timber, low-iron glass. Cool sky plus 2700–3200 K luminaires, separated into interior/exterior groups. Keep the building silhouette, window positions, perspective and image crop. Preserve blue exterior and warm interior separation; modest bloom.

## Golden hour · `golden-hour`

**Type:** lighting. **Atmosphere:** low warm sun.

- Palette: warm stone, oak, satin metal.
- Roughness starting range: 0.35–0.7; exceptions such as glass use their own measured shader.
- Relief starting range: 0.1–0.6 mm.
- Light: One low directional sun; warm key and cooler sky fill; choose shadow direction from reference.
- Camera: Frame for long shadows; retain focal length across variants.
- Finishing: Warm highlights, neutral midtones, soft shoulder.
- Acceptance: Sun direction agrees with shadows, reflections and illuminated facades.
- Failure to avoid: Do not turn all surfaces orange or paint shadows into albedo.

**Image prompt starter:** Reinterpret the supplied architectural reference as golden hour. Use warm stone, oak, satin metal. One low directional sun; warm key and cooler sky fill; choose shadow direction from reference. Keep the building silhouette, window positions, perspective and image crop. Warm highlights, neutral midtones, soft shoulder.

## Soft overcast · `overcast-soft`

**Type:** lighting. **Atmosphere:** diffuse overcast.

- Palette: pale concrete, weathered wood, matte stone.
- Roughness starting range: 0.5–0.85; exceptions such as glass use their own measured shader.
- Relief starting range: 0.2–1 mm.
- Light: Large diffuse sky, no strong direct sun; maintain contact and recess shading.
- Camera: Architectural perspective; add depth with occlusion and scale, not fake wide-angle stretch.
- Finishing: Soft contrast, restrained saturation.
- Acceptance: Open shadows retain depth; no hard cast sun shadow.
- Failure to avoid: Do not add ambient occlusion halos around every edge.

**Image prompt starter:** Reinterpret the supplied architectural reference as soft overcast. Use pale concrete, weathered wood, matte stone. Large diffuse sky, no strong direct sun; maintain contact and recess shading. Keep the building silhouette, window positions, perspective and image crop. Soft contrast, restrained saturation.

## Rainy cinematic · `rainy-cinematic`

**Type:** lighting. **Atmosphere:** wet dusk.

- Palette: wet stone, dark metal, coated glass.
- Roughness starting range: 0.08–0.6; exceptions such as glass use their own measured shader.
- Relief starting range: 0.1–0.6 mm.
- Light: Broad cool environment with warm practical sources; physically placed wetness masks.
- Camera: Keep horizon and reflections consistent; low camera only if requested.
- Finishing: Subtle haze and highlight bloom; retain readable blacks.
- Acceptance: Wetness pools in plausible areas; roughness varies with drainage/exposure.
- Failure to avoid: Do not make every surface a perfect mirror; rain must not change building geometry.

**Image prompt starter:** Reinterpret the supplied architectural reference as rainy cinematic. Use wet stone, dark metal, coated glass. Broad cool environment with warm practical sources; physically placed wetness masks. Keep the building silhouette, window positions, perspective and image crop. Subtle haze and highlight bloom; retain readable blacks.

## Architectural night · `night-architectural`

**Type:** lighting. **Atmosphere:** night.

- Palette: dark stone, emissive fixtures, transparent glazing.
- Roughness starting range: 0.25–0.7; exceptions such as glass use their own measured shader.
- Relief starting range: 0.1–0.8 mm.
- Light: Exterior fixtures, interior luminaires and environment in separate LightMix groups; finite output.
- Camera: Reference camera and visible fixture layout locked.
- Finishing: Control fireflies and clipping before denoising; gentle bloom.
- Acceptance: Light sources explain illuminated surfaces; unlit surfaces remain plausible.
- Failure to avoid: Do not use emission as a substitute for all indirect lighting.

**Image prompt starter:** Reinterpret the supplied architectural reference as architectural night. Use dark stone, emissive fixtures, transparent glazing. Exterior fixtures, interior luminaires and environment in separate LightMix groups; finite output. Keep the building silhouette, window positions, perspective and image crop. Control fireflies and clipping before denoising; gentle bloom.

## Scandinavian calm · `scandinavian`

**Type:** design. **Atmosphere:** soft daylight.

- Palette: light ash, wool, chalk plaster, muted grey.
- Roughness starting range: 0.5–0.9; exceptions such as glass use their own measured shader.
- Relief starting range: 0.05–0.4 mm.
- Light: Diffuse daylight and restrained 3000 K practicals.
- Camera: Eye-level, calm composition and moderate focal length.
- Finishing: Neutral whites, soft contrast, restrained warm timber.
- Acceptance: Wood grain has real scale; woven materials differ from plaster.
- Failure to avoid: Preserve floor plan; avoid sterile white clipping and generic oversized furniture.

**Image prompt starter:** Reinterpret the supplied architectural reference as scandinavian calm. Use light ash, wool, chalk plaster, muted grey. Diffuse daylight and restrained 3000 K practicals. Keep the building silhouette, window positions, perspective and image crop. Neutral whites, soft contrast, restrained warm timber.

## Japandi · `japandi`

**Type:** design. **Atmosphere:** filtered daylight.

- Palette: smoked oak, linen, clay, warm off-white.
- Roughness starting range: 0.55–0.9; exceptions such as glass use their own measured shader.
- Relief starting range: 0.1–0.7 mm.
- Light: Soft directional daylight, low contrast practicals; readable alcoves.
- Camera: Quiet framing, natural eye height; retain windows and circulation.
- Finishing: Earth palette, deep but open shadows.
- Acceptance: Tactile timber and linen, quiet joins, consistent low furniture scale.
- Failure to avoid: Do not invent shoji openings or lower ceiling heights to signal a style.

**Image prompt starter:** Reinterpret the supplied architectural reference as japandi. Use smoked oak, linen, clay, warm off-white. Soft directional daylight, low contrast practicals; readable alcoves. Keep the building silhouette, window positions, perspective and image crop. Earth palette, deep but open shadows.

## Warm minimalism · `warm-minimalism`

**Type:** design. **Atmosphere:** warm diffuse interior.

- Palette: travertine, walnut, boucle, cream plaster.
- Roughness starting range: 0.45–0.85; exceptions such as glass use their own measured shader.
- Relief starting range: 0.1–1 mm.
- Light: Concealed warm sources with broad daylight; avoid visible hot strips.
- Camera: Use reference composition and leave deliberate negative space.
- Finishing: Cream neutral balance; warm highlights without yellow whites.
- Acceptance: Fine plaster, porous stone and soft textiles are distinguishable in crop.
- Failure to avoid: Do not replace all texture with a uniform beige shader.

**Image prompt starter:** Reinterpret the supplied architectural reference as warm minimalism. Use travertine, walnut, boucle, cream plaster. Concealed warm sources with broad daylight; avoid visible hot strips. Keep the building silhouette, window positions, perspective and image crop. Cream neutral balance; warm highlights without yellow whites.

## Tactile brutalism · `brutalist`

**Type:** design. **Atmosphere:** raking overcast.

- Palette: board-formed concrete, dark steel, smoked glass.
- Roughness starting range: 0.55–0.9; exceptions such as glass use their own measured shader.
- Relief starting range: 0.3–2 mm.
- Light: Broad cool fill plus grazing light to show formwork relief; no exaggerated noise.
- Camera: Emphasize mass through framing, without altering locked structure.
- Finishing: Restrained saturation, controlled grey values.
- Acceptance: Formwork seams, tie-hole spacing and weathering follow construction logic.
- Failure to avoid: Do not add random holes everywhere or use centimetres of concrete displacement.

**Image prompt starter:** Reinterpret the supplied architectural reference as tactile brutalism. Use board-formed concrete, dark steel, smoked glass. Broad cool fill plus grazing light to show formwork relief; no exaggerated noise. Keep the building silhouette, window positions, perspective and image crop. Restrained saturation, controlled grey values.

## Contemporary Mediterranean · `mediterranean`

**Type:** design. **Atmosphere:** warm daylight.

- Palette: lime plaster, terracotta, pale stone, natural fibre.
- Roughness starting range: 0.55–0.95; exceptions such as glass use their own measured shader.
- Relief starting range: 0.2–1.5 mm.
- Light: Warm sun with open sky fill; shaded rooms remain cooler.
- Camera: Keep approved openings; arches require explicit geometry redesign scope.
- Finishing: Warm mineral palette; avoid oversaturated terracotta.
- Acceptance: Plaster relief and stone edge wear remain fine at full scale.
- Failure to avoid: Do not insert arches, pools or palms merely to force the aesthetic.

**Image prompt starter:** Reinterpret the supplied architectural reference as contemporary mediterranean. Use lime plaster, terracotta, pale stone, natural fibre. Warm sun with open sky fill; shaded rooms remain cooler. Keep the building silhouette, window positions, perspective and image crop. Warm mineral palette; avoid oversaturated terracotta.

## Industrial loft · `industrial-loft`

**Type:** design. **Atmosphere:** window daylight.

- Palette: brick, blackened steel, leather, reclaimed timber.
- Roughness starting range: 0.35–0.85; exceptions such as glass use their own measured shader.
- Relief starting range: 0.3–2 mm.
- Light: Strong window direction, soft fill, modest warm pendants.
- Camera: Match perspective and structural rhythm; avoid making every lens ultra-wide.
- Finishing: Balanced shadows; warm/cool materials separated.
- Acceptance: Brick courses and joints use measured dimensions; steel edges catch highlights.
- Failure to avoid: No invented exposed structure without a redesign instruction.

**Image prompt starter:** Reinterpret the supplied architectural reference as industrial loft. Use brick, blackened steel, leather, reclaimed timber. Strong window direction, soft fill, modest warm pendants. Keep the building silhouette, window positions, perspective and image crop. Balanced shadows; warm/cool materials separated.

## Biophilic tropical · `biophilic-tropical`

**Type:** design. **Atmosphere:** humid late afternoon.

- Palette: dense greenery, timber, pale concrete, water.
- Roughness starting range: 0.35–0.85; exceptions such as glass use their own measured shader.
- Relief starting range: 0.1–1 mm.
- Light: Filtered sun and sky; use layered vegetation, foliage transmission and gentle atmospheric depth.
- Camera: Preserve building visibility; set hero frame before scattering vegetation.
- Finishing: Natural varied greens; depth haze kept separate from geometry.
- Acceptance: Leaves vary in orientation, age and translucency; grass has no tile-grid repetition.
- Failure to avoid: No uniform green blobs, billboard foreground forest or excessive displacement on leaves.

**Image prompt starter:** Reinterpret the supplied architectural reference as biophilic tropical. Use dense greenery, timber, pale concrete, water. Filtered sun and sky; use layered vegetation, foliage transmission and gentle atmospheric depth. Keep the building silhouette, window positions, perspective and image crop. Natural varied greens; depth haze kept separate from geometry.

## Clay study · `clay-study`

**Type:** presentation. **Atmosphere:** studio soft.

- Palette: single neutral clay with optional glass exception.
- Roughness starting range: 0.65–0.85; exceptions such as glass use their own measured shader.
- Relief starting range: 0–0 mm.
- Light: Large soft key and fill; neutral environment; no texture-driven distraction.
- Camera: Reference camera for comparison; optional orthographic secondary view.
- Finishing: Linear-neutral lighting comparison, no stylized grading.
- Acceptance: Silhouette, reveals, openings and junctions stay legible.
- Failure to avoid: Do not claim a clay pass validates final materials or photorealism.

**Image prompt starter:** Reinterpret the supplied architectural reference as clay study. Use single neutral clay with optional glass exception. Large soft key and fill; neutral environment; no texture-driven distraction. Keep the building silhouette, window positions, perspective and image crop. Linear-neutral lighting comparison, no stylized grading.

## Watercolor concept · `watercolor-concept`

**Type:** presentation. **Atmosphere:** illustrative diffuse.

- Palette: paper grain, pigment washes, limited palette.
- Roughness starting range: 0.7–1; exceptions such as glass use their own measured shader.
- Relief starting range: 0–0 mm.
- Light: Render a clean structural base; use an image/illustration tool for wash and line treatment.
- Camera: Lock crop and key edges using guides; compare openings after stylization.
- Finishing: Paper and pigment treatment in a separate derived image.
- Acceptance: Building outline and openings survive the illustration pass.
- Failure to avoid: Not a native Corona preset. Do not substitute the illustration for an editable scene.

**Image prompt starter:** Reinterpret the supplied architectural reference as watercolor concept. Use paper grain, pigment washes, limited palette. Render a clean structural base; use an image/illustration tool for wash and line treatment. Keep the building silhouette, window positions, perspective and image crop. Paper and pigment treatment in a separate derived image.

## Technical axonometric · `technical-axonometric`

**Type:** presentation. **Atmosphere:** diagram studio.

- Palette: neutral surfaces, material category accents, linework.
- Roughness starting range: 0.65–0.9; exceptions such as glass use their own measured shader.
- Relief starting range: 0–0 mm.
- Light: Even readable illumination, soft grounding shadow; optional line pass via supported host.
- Camera: True orthographic camera; parallel world-axis lines remain parallel.
- Finishing: Clean white background and clear category separation.
- Acceptance: No perspective convergence; scale bar only when output scale is defined.
- Failure to avoid: A long focal length perspective is not a true axonometric projection.

**Image prompt starter:** Reinterpret the supplied architectural reference as technical axonometric. Use neutral surfaces, material category accents, linework. Even readable illumination, soft grounding shadow; optional line pass via supported host. Keep the building silhouette, window positions, perspective and image crop. Clean white background and clear category separation.
