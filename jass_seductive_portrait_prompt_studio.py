# JASS Seductive Portrait Prompt Studio
# 100 tasteful, non-explicit portrait prompts
# Requires: PySide6
# Run: python jass_seductive_portrait_prompt_studio.py

import sys, json, random
from pathlib import Path
from PySide6.QtCore import Qt, QTimer
from PySide6.QtGui import QFont, QKeySequence, QAction
from PySide6.QtWidgets import (
    QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout, QGridLayout,
    QListWidget, QListWidgetItem, QTextEdit, QLabel, QPushButton, QLineEdit,
    QComboBox, QMessageBox, QSplitter, QFrame, QCheckBox, QToolBar, QStatusBar
)

PROMPTS = [{'id': 1, 'title': 'Prompt 001', 'category': 'Featured', 'prompt': 'Transform my photo into a sophisticated, subtly seductive portrait. Keep my face, facial features, identity, and natural expression unchanged. Use warm cinematic lighting, soft shadows, slightly tousled hair, confident eye contact, and an elegant outfit that complements my appearance. Add a luxurious, intimate atmosphere with a softly blurred background, rich tones, gentle rim lighting, and a refined editorial photography style. The mood should feel confident, alluring, romantic, and mysterious — sensual rather than explicit, classy rather than provocative, photorealistic, high detail, natural skin texture.'}, {'id': 2, 'title': 'Prompt 002', 'category': 'Featured', 'prompt': 'Create a captivating, seductive portrait from my photo while preserving my exact face, identity, and natural features. Give me a confident, magnetic gaze toward the camera, softly parted lips, elegant posture, and a subtle expression of desire. Use warm golden-hour lighting, delicate shadows, silky highlights, and a luxurious evening setting with a softly blurred background. Style the outfit in a sophisticated, flattering way, with tasteful elegance and understated sensuality. Cinematic, intimate, glamorous, photorealistic, natural skin texture, refined editorial photography, mysterious and alluring mood.'}, {'id': 3, 'title': 'Prompt 003', 'category': 'Featured', 'prompt': 'Turn my photo into a sophisticated, irresistibly alluring portrait. Preserve my face, identity, facial features, and natural skin texture exactly. Give the image a confident, intimate mood with a subtle knowing smile and captivating eye contact. Use dramatic low-key lighting, warm highlights, soft shadows, slightly tousled hair, and an elegant evening setting. Add a luxurious, cinematic atmosphere with shallow depth of field and a beautifully blurred background. The overall feeling should be sensual, mysterious, confident, and romantic—tasteful glamour with understated seduction, photorealistic, high-end magazine portrait photography.'}, {'id': 4, 'title': 'Prompt 004', 'category': 'Featured', 'prompt': 'Create a captivating, sophisticated portrait from my photo while preserving my exact identity, face, facial features, and natural skin texture. Give me a calm, confident expression with captivating eye contact and a faint, playful smile. Place me in an elegant evening setting with soft moonlit ambience, warm highlights, gentle shadows, and a luxurious out-of-focus background. Add refined styling, natural tousled hair, cinematic depth of field, and high-end editorial photography. The mood should be sensual, mysterious, romantic, confident, and effortlessly alluring—tasteful, sophisticated, and photorealistic.'}, {'id': 5, 'title': 'Prompt 005', 'category': 'Featured', 'prompt': 'Turn my photo into a deeply alluring, cinematic portrait while preserving my exact identity, face, facial features, and natural appearance. Create an intimate nighttime atmosphere with soft ambient lighting, subtle highlights across the face, elegant shadows, and a luxurious setting. Give me relaxed confidence, intense eye contact, a subtle smile, and effortlessly charismatic body language. Style the scene with sophisticated evening fashion, slightly tousled hair, warm tones, shallow depth of field, and a soft atmospheric glow. Make it feel mysterious, romantic, confident, and irresistibly seductive—like a premium cinematic magazine portrait, photorealistic and naturally beautiful.'}, {'id': 6, 'title': 'Prompt 006', 'category': 'Featured', 'prompt': 'Transform my photo into an elegant, magnetic, subtly seductive portrait. Keep my face, identity, facial features, and body proportions completely natural and unchanged. Create an intimate evening atmosphere with soft candlelight, warm golden highlights, gentle shadows, and a luxurious blurred background. Give me relaxed, confident body language, direct captivating eye contact, and a subtle half-smile that conveys mystery and attraction. Add refined styling, tasteful clothing, cinematic depth of field, realistic skin texture, and high-end fashion-editorial photography. The mood should be sensual, sophisticated, romantic, and quietly irresistible—never explicit or exaggerated.'}, {'id': 7, 'title': 'Prompt 007', 'category': 'Featured', 'prompt': 'Create a mesmerizing, subtly seductive portrait from my photo while keeping my face, identity, and natural features completely authentic. Give me a calm, confident expression with captivating eye contact and a faint, playful smile. Place me in an elegant evening setting with soft moonlit ambience, warm highlights, gentle shadows, and a luxurious out-of-focus background. Add sophisticated styling, slightly tousled hair, cinematic lighting, shallow depth of field, realistic skin texture, and refined editorial photography. The mood should be intimate, mysterious, romantic, confident, and effortlessly alluring—tasteful, sophisticated, and photorealistic.'}, {'id': 8, 'title': 'Prompt 008', 'category': 'Featured', 'prompt': 'Create a sophisticated, intensely alluring portrait from my photo while preserving my exact identity, facial features, proportions, and natural appearance. Give me a confident, slightly playful gaze with a subtle smile and relaxed, elegant posture. Place me in a luxurious dimly lit setting with warm candlelight, soft golden reflections, delicate shadows, and a dreamy background. Add tasteful evening styling, natural hair movement, cinematic lighting, shallow depth of field, realistic skin texture, and subtle film-grain. The mood should be intimate, mysterious, romantic, and quietly seductive—classy, tasteful, photorealistic, and emotionally captivating.'}, {'id': 9, 'title': 'Prompt 009', 'category': 'Featured', 'prompt': 'Transform my photo into a glamorous, magnetic evening portrait with an understated seductive mood. Preserve my exact face, identity, facial structure, skin texture, and natural proportions. Give me a confident sideways glance toward the camera, a relaxed expression, and a subtle mischievous smile. Use dramatic cinematic lighting with warm highlights and soft shadows, an elegant nighttime setting, luxurious textures, and a softly blurred background. Add sophisticated fashion styling, natural hair movement, tasteful jewelry, and a polished editorial aesthetic. The final image should feel intimate, mysterious, confident, romantic, and irresistibly attractive—sensual without being explicit, photorealistic, refined, and cinematic.'}, {'id': 10, 'title': 'Prompt 010', 'category': 'Cinematic', 'prompt': 'Create a cinematic portrait from my photo with a mysterious, magnetic mood. Preserve my identity and facial features exactly. Use deep evening light, soft rim lighting, subtle haze, elegant styling, and a dramatic blurred background. The expression should be confident, intimate, and quietly alluring, like a scene from a sophisticated romance film. Photorealistic and natural.'}, {'id': 11, 'title': 'Prompt 011', 'category': 'Cinematic', 'prompt': 'Transform my photo into a premium movie-poster-style portrait. Keep my face completely recognizable and natural. Use warm practical lights, cinematic contrast, shallow depth of field, elegant wardrobe, and a confident gaze. The atmosphere should suggest attraction and mystery without becoming explicit.'}, {'id': 12, 'title': 'Prompt 012', 'category': 'Cinematic', 'prompt': 'Give my photo a cinematic midnight atmosphere. Preserve my face and proportions. Add soft blue ambient light balanced with warm highlights, gentle shadows, rain-speckled glass in the background, and an intense but natural gaze. Elegant, romantic, mysterious, photorealistic.'}, {'id': 13, 'title': 'Prompt 013', 'category': 'Cinematic', 'prompt': 'Turn my portrait into a sophisticated film-noir-inspired image. Keep my identity unchanged. Use directional light, subtle shadow patterns, classic evening styling, and a confident expression. Make it alluring, mysterious, tasteful, and cinematic.'}, {'id': 14, 'title': 'Prompt 014', 'category': 'Cinematic', 'prompt': 'Create a luxurious cinematic close-up from my photo. Preserve every important facial characteristic. Use soft golden backlighting, realistic skin, a shallow focus background, elegant clothing, and a restrained, knowing smile. Romantic, magnetic, sophisticated.'}, {'id': 15, 'title': 'Prompt 015', 'category': 'Cinematic', 'prompt': 'Make my photo look like a frame from a beautifully photographed romantic drama. Preserve my face exactly. Add warm practical lighting, elegant surroundings, subtle atmosphere, confident eye contact, and natural emotion. Sophisticated and photorealistic.'}, {'id': 16, 'title': 'Prompt 016', 'category': 'Cinematic', 'prompt': 'Create a cinematic rooftop-at-night portrait from my photo. Keep my identity unchanged. Add city lights, gentle wind in the hair, sophisticated evening clothing, warm rim lighting, and an understated confident expression. Romantic, modern, alluring.'}, {'id': 17, 'title': 'Prompt 017', 'category': 'Cinematic', 'prompt': 'Transform my photo into a cinematic hotel-lounge portrait. Preserve my face and natural appearance. Use amber lighting, luxurious textures, soft bokeh, elegant posture, and a subtle smile. The mood should be intimate, confident, romantic, and refined.'}, {'id': 18, 'title': 'Prompt 018', 'category': 'Cinematic', 'prompt': 'Create a cinematic portrait beside a rain-covered window. Preserve my exact identity. Use soft window light, warm interior tones, slightly tousled hair, sophisticated styling, and a contemplative yet alluring gaze. Natural, emotional, photorealistic.'}, {'id': 19, 'title': 'Prompt 019', 'category': 'Candlelight & Warmth', 'prompt': 'Create a warm candlelit portrait from my photo. Preserve my exact face and natural features. Use flickering candlelight, soft shadows, warm highlights, elegant evening styling, and a subtle confident smile. Romantic, intimate, tasteful, photorealistic.'}, {'id': 20, 'title': 'Prompt 020', 'category': 'Candlelight & Warmth', 'prompt': 'Place my portrait in an elegant candlelit dinner setting. Keep my identity unchanged. Add glowing candles, refined table details, soft background bokeh, warm skin tones, and captivating eye contact. Sophisticated romantic atmosphere.'}, {'id': 21, 'title': 'Prompt 021', 'category': 'Candlelight & Warmth', 'prompt': 'Transform my photo into a candlelit luxury-suite portrait. Preserve my face and proportions. Use warm ambient illumination, delicate shadows, silk-like textures in the environment, and a relaxed confident expression. Sensual through atmosphere, not exposure.'}, {'id': 22, 'title': 'Prompt 022', 'category': 'Candlelight & Warmth', 'prompt': 'Create an intimate portrait illuminated by dozens of soft candles in the background. Keep my facial features authentic. Add warm rim light, natural skin texture, elegant clothing, and a gentle knowing smile. Luxurious and romantic.'}, {'id': 23, 'title': 'Prompt 023', 'category': 'Candlelight & Warmth', 'prompt': 'Give my photo a warm amber glow as though photographed during an intimate evening gathering. Preserve my identity. Use candlelight reflections, shallow depth of field, elegant styling, and direct but relaxed eye contact.'}, {'id': 24, 'title': 'Prompt 024', 'category': 'Candlelight & Warmth', 'prompt': 'Create a sophisticated portrait beside a fireplace. Keep my face exactly recognizable. Use warm firelight, soft shadows, luxurious surroundings, relaxed posture, and a subtle smile. Romantic, alluring, and natural.'}, {'id': 25, 'title': 'Prompt 025', 'category': 'Candlelight & Warmth', 'prompt': 'Transform my photo into an elegant candlelit lounge portrait. Preserve my identity and realistic skin texture. Add warm bokeh, tasteful jewelry, refined evening clothing, and a confident expression.'}, {'id': 26, 'title': 'Prompt 026', 'category': 'Candlelight & Warmth', 'prompt': 'Create a cozy evening portrait with candles, soft blankets, and warm ambient light in the background. Keep my face unchanged. Make the expression confident, intimate, and gently playful. Photorealistic and sophisticated.'}, {'id': 27, 'title': 'Prompt 027', 'category': 'Candlelight & Warmth', 'prompt': 'Create a romantic candlelit close-up with soft golden illumination across my face. Preserve every facial detail. Add elegant styling, shallow focus, natural skin texture, and a subtle magnetic gaze.'}, {'id': 28, 'title': 'Prompt 028', 'category': 'Moonlight & Night', 'prompt': 'Transform my photo into a moonlit portrait. Preserve my exact identity and natural features. Use soft silver-blue light, gentle shadows, a dark elegant background, and warm highlights around the face. Calm, mysterious, romantic, and alluring.'}, {'id': 29, 'title': 'Prompt 029', 'category': 'Moonlight & Night', 'prompt': 'Create a sophisticated nighttime balcony portrait from my photo. Keep my face unchanged. Add moonlight, distant city bokeh, a gentle breeze, elegant evening clothing, and confident eye contact. Cinematic and photorealistic.'}, {'id': 30, 'title': 'Prompt 030', 'category': 'Moonlight & Night', 'prompt': 'Place me in a moonlit garden at night. Preserve my identity and natural proportions. Use soft lunar illumination, subtle foliage shadows, dreamy bokeh, and a calm confident expression. Romantic and mysterious.'}, {'id': 31, 'title': 'Prompt 031', 'category': 'Moonlight & Night', 'prompt': 'Create a luxurious rooftop portrait under moonlight. Keep my face authentic. Add soft city lights, cool ambient tones, warm edge lighting, and relaxed confident posture. Refined and cinematic.'}, {'id': 32, 'title': 'Prompt 032', 'category': 'Moonlight & Night', 'prompt': 'Turn my photo into an elegant portrait beside a moonlit window. Preserve facial features exactly. Use cool night light balanced by a warm interior glow, soft shadows, and a quiet knowing expression.'}, {'id': 33, 'title': 'Prompt 033', 'category': 'Moonlight & Night', 'prompt': 'Create a mysterious nighttime portrait with distant stars and subtle atmospheric haze. Keep my identity unchanged. Use elegant styling, natural skin texture, and captivating but relaxed eye contact.'}, {'id': 34, 'title': 'Prompt 034', 'category': 'Moonlight & Night', 'prompt': 'Transform my photo into a sophisticated after-dark editorial portrait. Preserve my face. Use deep shadows, silver highlights, tasteful evening clothing, and a confident half-smile. High-end fashion photography.'}, {'id': 35, 'title': 'Prompt 035', 'category': 'Moonlight & Night', 'prompt': 'Create a romantic city-night portrait from my photo. Keep my features natural. Use neon bokeh far in the background, soft skin lighting, elegant styling, and an understated magnetic gaze.'}, {'id': 36, 'title': 'Prompt 036', 'category': 'Moonlight & Night', 'prompt': 'Create a serene midnight portrait with moonlight filtering through curtains. Preserve my exact face and proportions. Use soft shadows, luxurious textures, and an intimate but tasteful atmosphere.'}, {'id': 37, 'title': 'Prompt 037', 'category': 'Luxury Editorial', 'prompt': 'Turn my photo into a high-fashion editorial portrait. Preserve my exact identity. Use sophisticated wardrobe styling, sculpted studio light, subtle shadows, luxurious textures, and a confident expression. Elegant, alluring, photorealistic.'}, {'id': 38, 'title': 'Prompt 038', 'category': 'Luxury Editorial', 'prompt': 'Create a luxury magazine cover portrait from my photo. Keep my face and natural features unchanged. Use polished studio lighting, refined styling, tasteful jewelry, and a magnetic gaze. Premium editorial aesthetic.'}, {'id': 39, 'title': 'Prompt 039', 'category': 'Luxury Editorial', 'prompt': 'Transform my portrait into an upscale fashion campaign image. Preserve identity and realistic skin texture. Add elegant clothing, dramatic but flattering lighting, clean composition, and a subtle knowing smile.'}, {'id': 40, 'title': 'Prompt 040', 'category': 'Luxury Editorial', 'prompt': 'Create a couture-inspired evening portrait while keeping my face completely authentic. Use sophisticated fabrics, cinematic lighting, elegant posture, and restrained sensuality. Photorealistic luxury editorial.'}, {'id': 41, 'title': 'Prompt 041', 'category': 'Luxury Editorial', 'prompt': 'Give my photo a premium fragrance-advertisement aesthetic. Preserve my identity. Use soft golden lighting, luxurious surroundings, elegant styling, and an enigmatic expression. Sophisticated and alluring.'}, {'id': 42, 'title': 'Prompt 042', 'category': 'Luxury Editorial', 'prompt': 'Create a high-end beauty editorial portrait from my photo. Keep facial proportions and skin texture natural. Use flattering softbox light, subtle highlights, elegant hair styling, and confident eye contact.'}, {'id': 43, 'title': 'Prompt 043', 'category': 'Luxury Editorial', 'prompt': 'Transform my photo into an elegant black-tie editorial portrait. Preserve my face exactly. Add sophisticated wardrobe, dramatic background bokeh, refined lighting, and a calm magnetic expression.'}, {'id': 44, 'title': 'Prompt 044', 'category': 'Luxury Editorial', 'prompt': 'Create a luxury hotel campaign portrait from my photo. Preserve identity and natural appearance. Use marble, velvet, warm lighting, elegant styling, and relaxed confident posture.'}, {'id': 45, 'title': 'Prompt 045', 'category': 'Luxury Editorial', 'prompt': 'Create an upscale evening fashion portrait with a subtle seductive mood. Keep my face unchanged. Use sophisticated wardrobe, polished lighting, natural texture, and a mysterious gaze.'}, {'id': 46, 'title': 'Prompt 046', 'category': 'Soft Romantic', 'prompt': 'Create a soft romantic portrait from my photo. Preserve my exact face and natural features. Use diffused golden light, gentle pastel tones, soft background blur, and a warm affectionate expression. Elegant and photorealistic.'}, {'id': 47, 'title': 'Prompt 047', 'category': 'Soft Romantic', 'prompt': 'Transform my photo into a dreamy romantic portrait at sunset. Keep my identity unchanged. Add glowing backlight, soft wind in the hair, warm bokeh, elegant styling, and a subtle smile.'}, {'id': 48, 'title': 'Prompt 048', 'category': 'Soft Romantic', 'prompt': 'Create a tender but alluring portrait beside a window at golden hour. Preserve my facial features. Use soft natural light, gentle shadows, elegant clothing, and relaxed eye contact.'}, {'id': 49, 'title': 'Prompt 049', 'category': 'Soft Romantic', 'prompt': 'Give my photo a dreamy garden setting at dusk. Keep my face exactly recognizable. Add soft flowers, warm light, shallow depth of field, and a calm confident expression.'}, {'id': 50, 'title': 'Prompt 050', 'category': 'Soft Romantic', 'prompt': 'Create a romantic portrait surrounded by softly glowing fairy lights. Preserve my identity and natural skin. Use warm illumination, elegant styling, and a subtle playful smile.'}, {'id': 51, 'title': 'Prompt 051', 'category': 'Soft Romantic', 'prompt': 'Transform my photo into an intimate sunset portrait beside the sea. Keep my facial features unchanged. Add warm sky colors, gentle breeze, natural hair movement, and a confident relaxed gaze.'}, {'id': 52, 'title': 'Prompt 052', 'category': 'Soft Romantic', 'prompt': 'Create a sophisticated romantic portrait with soft rose-toned ambient light. Preserve my identity. Use subtle shadows, elegant styling, realistic skin texture, and a quiet magnetic expression.'}, {'id': 53, 'title': 'Prompt 053', 'category': 'Soft Romantic', 'prompt': 'Create a beautiful evening garden portrait with warm lanterns and soft foliage bokeh. Keep my face authentic. Add elegant clothing and a subtle, knowing smile.'}, {'id': 54, 'title': 'Prompt 054', 'category': 'Soft Romantic', 'prompt': 'Turn my photo into a romantic editorial portrait with soft light and dreamy atmosphere. Preserve my exact identity, use tasteful styling, and emphasize natural expression and eye contact.'}, {'id': 55, 'title': 'Prompt 055', 'category': 'Confident & Magnetic', 'prompt': 'Transform my photo into a confident, magnetic portrait. Preserve my exact identity and facial features. Give me direct eye contact, relaxed shoulders, elegant styling, and dramatic but flattering lighting. The mood should be powerful, sophisticated, and subtly alluring.'}, {'id': 56, 'title': 'Prompt 056', 'category': 'Confident & Magnetic', 'prompt': 'Create a portrait that communicates quiet confidence and irresistible charisma. Keep my face unchanged. Use clean cinematic lighting, sophisticated clothing, subtle background blur, and a slight knowing smile.'}, {'id': 57, 'title': 'Prompt 057', 'category': 'Confident & Magnetic', 'prompt': 'Give my photo a bold editorial attitude while preserving my natural appearance. Use strong eye contact, elegant posture, controlled shadows, and premium fashion styling. Confident, magnetic, photorealistic.'}, {'id': 58, 'title': 'Prompt 058', 'category': 'Confident & Magnetic', 'prompt': 'Create a sophisticated portrait with a playful, confident gaze. Preserve my face and natural skin texture. Add warm studio light, elegant wardrobe, shallow depth of field, and a polished editorial finish.'}, {'id': 59, 'title': 'Prompt 059', 'category': 'Confident & Magnetic', 'prompt': 'Transform my photo into a charismatic evening portrait. Keep identity unchanged. Use dramatic rim lighting, relaxed posture, subtle smile, and luxurious surroundings. Tasteful and alluring.'}, {'id': 60, 'title': 'Prompt 060', 'category': 'Confident & Magnetic', 'prompt': 'Create a portrait with quiet self-assurance. Preserve facial features exactly. Use minimalist luxury styling, soft directional light, and a calm but captivating gaze.'}, {'id': 61, 'title': 'Prompt 061', 'category': 'Confident & Magnetic', 'prompt': 'Turn my photo into a powerful fashion portrait with understated sensuality. Keep my face natural. Use sophisticated styling, cinematic contrast, and confident body language.'}, {'id': 62, 'title': 'Prompt 062', 'category': 'Confident & Magnetic', 'prompt': 'Create an elegant portrait with a playful sideways glance. Preserve my identity. Add warm light, luxurious textures, and a softly blurred background. Charming, confident, and alluring.'}, {'id': 63, 'title': 'Prompt 063', 'category': 'Confident & Magnetic', 'prompt': 'Create a magnetic close-up portrait with direct eye contact and a subtle half-smile. Preserve every facial detail. Use soft cinematic lighting and high-end editorial styling.'}, {'id': 64, 'title': 'Prompt 064', 'category': 'Glamorous Evening', 'prompt': 'Create a glamorous evening portrait from my photo. Preserve my exact identity. Use sophisticated evening wear, sparkling background bokeh, warm cinematic lighting, elegant posture, and a confident expression.'}, {'id': 65, 'title': 'Prompt 065', 'category': 'Glamorous Evening', 'prompt': 'Transform my photo into a luxurious gala portrait. Keep my face natural and unchanged. Add elegant lighting, refined jewelry, tasteful evening styling, and a magnetic gaze.'}, {'id': 66, 'title': 'Prompt 066', 'category': 'Glamorous Evening', 'prompt': 'Create a sophisticated cocktail-lounge portrait. Preserve identity and skin texture. Use amber lighting, polished interiors, elegant clothing, and a subtle playful expression.'}, {'id': 67, 'title': 'Prompt 067', 'category': 'Glamorous Evening', 'prompt': 'Give my photo a glamorous red-carpet aesthetic without changing my face. Use flattering cinematic light, elegant styling, sophisticated background bokeh, and confident eye contact.'}, {'id': 68, 'title': 'Prompt 068', 'category': 'Glamorous Evening', 'prompt': 'Create a luxury ballroom portrait from my photo. Keep my facial features authentic. Add warm chandeliers, elegant evening clothing, soft shadows, and an understated romantic mood.'}, {'id': 69, 'title': 'Prompt 069', 'category': 'Glamorous Evening', 'prompt': 'Transform my portrait into a glamorous rooftop dinner scene. Preserve my face. Use city lights, warm practical lighting, elegant styling, and relaxed confident body language.'}, {'id': 70, 'title': 'Prompt 070', 'category': 'Glamorous Evening', 'prompt': 'Create a sophisticated evening portrait beside a grand staircase. Keep identity unchanged. Use cinematic lighting, luxurious architecture, elegant wardrobe, and a subtle smile.'}, {'id': 71, 'title': 'Prompt 071', 'category': 'Glamorous Evening', 'prompt': 'Create a polished night-out portrait with refined styling and soft bokeh. Preserve natural facial features. Make the mood confident, glamorous, romantic, and tasteful.'}, {'id': 72, 'title': 'Prompt 072', 'category': 'Glamorous Evening', 'prompt': 'Turn my photo into a luxury evening campaign image. Preserve identity and proportions. Add elegant surroundings, warm highlights, and a mysterious confident gaze.'}, {'id': 73, 'title': 'Prompt 073', 'category': 'Nature & Travel', 'prompt': 'Transform my photo into a romantic sunset portrait on a Mediterranean terrace. Preserve my face exactly. Add warm sunlight, gentle breeze, elegant clothing, and a relaxed confident gaze.'}, {'id': 74, 'title': 'Prompt 074', 'category': 'Nature & Travel', 'prompt': 'Create a sophisticated beach-at-dusk portrait. Keep my identity and facial features unchanged. Use soft sunset light, natural wind, elegant styling, and cinematic depth of field.'}, {'id': 75, 'title': 'Prompt 075', 'category': 'Nature & Travel', 'prompt': 'Place my portrait in a luxurious mountain lodge at twilight. Preserve my face. Add warm interior light, soft window reflections, elegant clothing, and a calm magnetic expression.'}, {'id': 76, 'title': 'Prompt 076', 'category': 'Nature & Travel', 'prompt': 'Create a romantic garden portrait surrounded by lush greenery. Keep my identity unchanged. Use dappled sunlight, soft shadows, elegant styling, and a subtle knowing smile.'}, {'id': 77, 'title': 'Prompt 077', 'category': 'Nature & Travel', 'prompt': 'Transform my photo into an elegant lakeside evening portrait. Preserve facial features. Use reflections, warm twilight light, sophisticated clothing, and relaxed eye contact.'}, {'id': 78, 'title': 'Prompt 078', 'category': 'Nature & Travel', 'prompt': 'Create a cinematic portrait on a quiet tropical terrace at sunset. Keep my face natural. Add soft palm silhouettes, warm light, elegant styling, and a confident expression.'}, {'id': 79, 'title': 'Prompt 079', 'category': 'Nature & Travel', 'prompt': 'Create a sophisticated European street portrait at blue hour. Preserve my identity. Add warm café lights, elegant evening fashion, soft rain reflections, and magnetic eye contact.'}, {'id': 80, 'title': 'Prompt 080', 'category': 'Nature & Travel', 'prompt': 'Transform my photo into a romantic vineyard-at-sunset portrait. Keep facial features authentic. Use golden light, soft background blur, elegant clothing, and natural confidence.'}, {'id': 81, 'title': 'Prompt 081', 'category': 'Nature & Travel', 'prompt': 'Create a beautiful coastal evening portrait with distant lights and gentle ocean haze. Preserve my exact face. Make the mood romantic, mysterious, and subtly alluring.'}, {'id': 82, 'title': 'Prompt 082', 'category': 'Classic Portrait', 'prompt': 'Create a timeless studio portrait from my photo. Preserve my exact face and natural features. Use classic soft lighting, elegant clothing, neutral background, confident eye contact, and subtle cinematic contrast.'}, {'id': 83, 'title': 'Prompt 083', 'category': 'Classic Portrait', 'prompt': 'Transform my photo into a classic Hollywood-inspired portrait. Keep my identity unchanged. Use glamorous but tasteful lighting, elegant styling, gentle shadows, and a confident expression.'}, {'id': 84, 'title': 'Prompt 084', 'category': 'Classic Portrait', 'prompt': 'Create a refined black-and-white portrait from my photo. Preserve facial details and identity. Use dramatic studio lighting, elegant posture, and an expressive, magnetic gaze.'}, {'id': 85, 'title': 'Prompt 085', 'category': 'Classic Portrait', 'prompt': 'Give my photo a classic portrait-photography aesthetic. Keep my face completely authentic. Use soft directional light, sophisticated clothing, clean background, and a subtle smile.'}, {'id': 86, 'title': 'Prompt 086', 'category': 'Classic Portrait', 'prompt': 'Create an elegant monochrome editorial portrait. Preserve natural skin texture and facial proportions. Use controlled shadows, refined styling, and captivating eye contact.'}, {'id': 87, 'title': 'Prompt 087', 'category': 'Classic Portrait', 'prompt': 'Transform my photo into a timeless magazine portrait. Keep identity unchanged. Use soft studio light, tasteful wardrobe, natural expression, and premium photographic detail.'}, {'id': 88, 'title': 'Prompt 088', 'category': 'Classic Portrait', 'prompt': 'Create a classic close-up portrait with beautiful catchlights in the eyes. Preserve my exact features. Use flattering soft light, subtle shadows, and an understated confident smile.'}, {'id': 89, 'title': 'Prompt 089', 'category': 'Classic Portrait', 'prompt': 'Create a sophisticated portrait inspired by vintage cinema. Keep my face natural. Use elegant styling, controlled contrast, subtle film grain, and a mysterious expression.'}, {'id': 90, 'title': 'Prompt 090', 'category': 'Classic Portrait', 'prompt': 'Turn my photo into a timeless romantic portrait with classic studio lighting. Preserve identity, natural texture, and proportions. Refined, elegant, and subtly alluring.'}, {'id': 91, 'title': 'Prompt 091', 'category': 'Dreamy & Artistic', 'prompt': 'Create a dreamy cinematic portrait from my photo. Preserve my exact identity. Add soft atmospheric haze, glowing highlights, shallow depth of field, elegant styling, and a mysterious confident gaze.'}, {'id': 92, 'title': 'Prompt 092', 'category': 'Dreamy & Artistic', 'prompt': 'Transform my portrait into a sophisticated dreamscape with soft bokeh and gentle light leaks. Keep my face unchanged. Romantic, elegant, photorealistic, and subtly alluring.'}, {'id': 93, 'title': 'Prompt 093', 'category': 'Dreamy & Artistic', 'prompt': 'Create an artistic portrait with floating warm lights in the background. Preserve facial features and natural skin. Use soft cinematic illumination and a calm magnetic expression.'}, {'id': 94, 'title': 'Prompt 094', 'category': 'Dreamy & Artistic', 'prompt': 'Give my photo a dreamy twilight atmosphere with subtle mist. Keep my identity authentic. Add elegant clothing, warm highlights, and an intimate confident gaze.'}, {'id': 95, 'title': 'Prompt 095', 'category': 'Dreamy & Artistic', 'prompt': 'Create a luxurious soft-focus portrait while keeping my face sharp and recognizable. Use glowing background light, delicate shadows, elegant styling, and understated romance.'}, {'id': 96, 'title': 'Prompt 096', 'category': 'Dreamy & Artistic', 'prompt': 'Transform my photo into a cinematic dream sequence. Preserve identity and proportions. Use ethereal light, sophisticated wardrobe, atmospheric depth, and a subtle knowing smile.'}, {'id': 97, 'title': 'Prompt 097', 'category': 'Dreamy & Artistic', 'prompt': 'Create an artistic portrait with beautiful lens flare and golden haze. Keep my facial features natural. Use refined styling and relaxed, confident eye contact.'}, {'id': 98, 'title': 'Prompt 098', 'category': 'Dreamy & Artistic', 'prompt': 'Create a dreamy night portrait with soft floating lights and gentle atmospheric glow. Preserve my exact face. Romantic, mysterious, sophisticated, photorealistic.'}, {'id': 99, 'title': 'Prompt 099', 'category': 'Dreamy & Artistic', 'prompt': 'Turn my photo into a premium fine-art portrait with cinematic atmosphere. Preserve identity, realistic skin texture, elegant styling, and a quietly magnetic expression.'}, {'id': 100, 'title': 'Prompt 100', 'category': 'Signature', 'prompt': 'Transform my photo into an unforgettable signature portrait. Preserve my exact identity, facial features, natural proportions, and realistic skin texture. Combine sophisticated evening styling, warm cinematic light, subtle shadows, beautiful background bokeh, confident eye contact, and a restrained knowing smile. The atmosphere should feel luxurious, romantic, mysterious, magnetic, and subtly seductive—elegant rather than explicit, photorealistic, polished, and worthy of a premium magazine cover.'}]

class PromptStudio(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("JASS Seductive Portrait Prompt Studio")
        self.resize(1250, 780)
        self.favorites = set()
        self.filtered = []
        self.build_ui()
        self.apply_theme()
        self.refresh()
        self.select_row(0)

    def build_ui(self):
        central = QWidget()
        root = QVBoxLayout(central)
        root.setContentsMargins(18, 18, 18, 14)
        root.setSpacing(12)

        title_row = QHBoxLayout()
        title = QLabel("JASS Seductive Portrait Prompt Studio")
        title.setObjectName("title")
        subtitle = QLabel("100 tasteful • cinematic • romantic • alluring prompts")
        subtitle.setObjectName("subtitle")
        title_row.addWidget(title)
        title_row.addStretch()
        title_row.addWidget(subtitle)
        root.addLayout(title_row)

        controls = QHBoxLayout()
        self.search = QLineEdit()
        self.search.setPlaceholderText("Search prompts, moods, lighting, settings...")
        self.search.textChanged.connect(self.refresh)
        controls.addWidget(self.search, 3)

        self.category = QComboBox()
        self.category.addItem("All categories")
        cats = sorted(set(x["category"] for x in PROMPTS))
        self.category.addItems(cats)
        self.category.currentTextChanged.connect(self.refresh)
        controls.addWidget(self.category, 1)

        self.fav_only = QCheckBox("Favorites only")
        self.fav_only.stateChanged.connect(self.refresh)
        controls.addWidget(self.fav_only)

        root.addLayout(controls)

        splitter = QSplitter(Qt.Horizontal)

        left = QFrame()
        left.setObjectName("panel")
        ll = QVBoxLayout(left)
        self.list = QListWidget()
        self.list.currentRowChanged.connect(self.select_row)
        ll.addWidget(self.list)
        splitter.addWidget(left)

        right = QFrame()
        right.setObjectName("panel")
        rl = QVBoxLayout(right)

        self.prompt_title = QLabel("Select a prompt")
        self.prompt_title.setObjectName("promptTitle")
        self.meta = QLabel("")
        self.meta.setObjectName("meta")
        rl.addWidget(self.prompt_title)
        rl.addWidget(self.meta)

        self.editor = QTextEdit()
        self.editor.setPlaceholderText("Your prompt will appear here...")
        rl.addWidget(self.editor, 1)

        buttons = QHBoxLayout()
        self.copy_btn = QPushButton("Copy Prompt")
        self.copy_btn.clicked.connect(self.copy_prompt)
        self.favorite_btn = QPushButton("☆ Favorite")
        self.favorite_btn.clicked.connect(self.toggle_favorite)
        self.random_btn = QPushButton("Random")
        self.random_btn.clicked.connect(self.random_prompt)
        self.save_btn = QPushButton("Save Edit")
        self.save_btn.clicked.connect(self.save_edit)
        buttons.addWidget(self.copy_btn)
        buttons.addWidget(self.favorite_btn)
        buttons.addWidget(self.random_btn)
        buttons.addStretch()
        buttons.addWidget(self.save_btn)
        rl.addLayout(buttons)

        splitter.addWidget(right)
        splitter.setSizes([360, 820])
        root.addWidget(splitter, 1)

        tip = QLabel("Tip: Select a prompt, customize the wording, then Copy Prompt and paste it into your image-generation workflow.")
        tip.setObjectName("tip")
        root.addWidget(tip)

        self.setCentralWidget(central)
        self.setStatusBar(QStatusBar())

        # Shortcuts
        copy_action = QAction(self)
        copy_action.setShortcut(QKeySequence("Ctrl+C"))
        copy_action.triggered.connect(self.copy_prompt)
        self.addAction(copy_action)

    def apply_theme(self):
        self.setStyleSheet("""
            QMainWindow, QWidget { background: #15131a; color: #eeeaf2; }
            #title { font-size: 25px; font-weight: 700; }
            #subtitle { color: #b9a8c7; font-size: 13px; }
            #panel { background: #1e1a24; border: 1px solid #342b3e; border-radius: 12px; }
            QLineEdit, QComboBox, QTextEdit, QListWidget {
                background: #17151b; color: #eeeaf2; border: 1px solid #403447;
                border-radius: 8px; padding: 8px;
            }
            QListWidget::item { padding: 10px; border-bottom: 1px solid #29232f; }
            QListWidget::item:selected { background: #4a3457; }
            #promptTitle { font-size: 21px; font-weight: 700; }
            #meta { color: #b9a8c7; }
            QPushButton {
                background: #3b2a46; color: #fff; border: 1px solid #60466f;
                padding: 9px 14px; border-radius: 8px;
            }
            QPushButton:hover { background: #523763; }
            #tip { color: #a99dad; padding: 4px; }
            QCheckBox { color: #cfc5d5; }
        """)

    def refresh(self):
        query = self.search.text().strip().lower()
        cat = self.category.currentText()
        self.list.blockSignals(True)
        self.list.clear()
        self.filtered = []
        for p in PROMPTS:
            hay = (p["title"] + " " + p["category"] + " " + p["prompt"]).lower()
            if query and query not in hay:
                continue
            if cat != "All categories" and p["category"] != cat:
                continue
            if self.fav_only.isChecked() and p["id"] not in self.favorites:
                continue
            self.filtered.append(p)
            star = " ★" if p["id"] in self.favorites else ""
            item = QListWidgetItem(f'{p["id"]:03d}  {p["category"]}{star}')
            self.list.addItem(item)
        self.list.blockSignals(False)
        self.statusBar().showMessage(f"{len(self.filtered)} prompts shown • 100 total")

    def select_row(self, row):
        if row < 0 or row >= len(self.filtered):
            return
        p = self.filtered[row]
        self.prompt_title.setText(f'{p["id"]:03d} — {p["category"]}')
        self.meta.setText(f'{p["category"]}  •  Prompt {p["id"]} of 100')
        self.editor.setPlainText(p["prompt"])
        self.update_favorite_button(p["id"])

    def current_prompt(self):
        row = self.list.currentRow()
        if 0 <= row < len(self.filtered):
            return self.filtered[row]
        return None

    def update_favorite_button(self, pid):
        self.favorite_btn.setText("★ Favorited" if pid in self.favorites else "☆ Favorite")

    def copy_prompt(self):
        p = self.current_prompt()
        if not p:
            return
        QApplication.clipboard().setText(self.editor.toPlainText())
        self.statusBar().showMessage("Prompt copied to clipboard", 2500)

    def toggle_favorite(self):
        p = self.current_prompt()
        if not p:
            return
        if p["id"] in self.favorites:
            self.favorites.remove(p["id"])
        else:
            self.favorites.add(p["id"])
        self.update_favorite_button(p["id"])
        self.refresh()
        # restore selected prompt if possible
        for i, x in enumerate(self.filtered):
            if x["id"] == p["id"]:
                self.list.setCurrentRow(i)
                break

    def random_prompt(self):
        if not self.filtered:
            return
        row = random.randrange(len(self.filtered))
        self.list.setCurrentRow(row)

    def save_edit(self):
        p = self.current_prompt()
        if not p:
            return
        p["prompt"] = self.editor.toPlainText().strip()
        self.statusBar().showMessage("Prompt edited for this session", 2500)

def main():
    app = QApplication(sys.argv)
    app.setApplicationName("JASS Seductive Portrait Prompt Studio")
    win = PromptStudio()
    win.show()
    sys.exit(app.exec())

if __name__ == "__main__":
    main()
