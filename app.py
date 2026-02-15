from flask import Flask, render_template, request, redirect, url_for, make_response

app = Flask(__name__)

TRANSLATIONS = {
    "en": {
        # ===== NAV =====
        "nav_menu": "Menu",
        "nav_rules": "Rules",
        "nav_news": "News",
        "nav_language": "Language",

        # ===== HEADER LINKS =====
        "home_about": "About",
        "home_contacts": "Contacts",
        "home_booking": "Booking",

        # ===== FOOTER =====
        "footer_contacts": "CONTACTS",

        # ===== HOME =====
        "home_title": "About Moscow Restaurant",
        "home_philosophy_title": "Our Philosophy",
        "home_philosophy_text": "Moscow Restaurant is a refined fine-dining destination where tradition meets modern culinary artistry. Inspired by European haute cuisine and enriched with Russian heritage, we create dishes that celebrate depth, precision, and emotion.",
        "home_craft_title": "Culinary Craftsmanship",
        "home_craft_text": "Our philosophy is built on carefully selected seasonal ingredients, balanced flavors, and impeccable presentation. Each plate is crafted not only to satisfy, but to tell a story — where every texture, aroma, and detail is part of the experience.",
        "home_chef_title": "Meet the Chef",
        "home_chef_text": "At the heart of our kitchen stands Chef Aleksandr Morozov — a visionary culinary artist trained in Michelin-starred establishments across Europe. His approach blends classical technique with contemporary creativity, transforming every dish into a sensory experience.",
        "home_beyond_text": "Beyond the cuisine, Moscow Restaurant offers an atmosphere of understated luxury: warm lighting, refined interiors, and an intimate setting designed for unforgettable evenings. Here, time slows down — and every dinner becomes a moment worth remembering.",
        "home_wine_title": "A Curated Wine Experience",
        "home_wine_text": "Our wine collection is curated with the same dedication as our cuisine. Featuring rare vintages and prestigious labels from France, Italy, and Spain, each selection is chosen to elevate the tasting journey and perfectly complement the depth of our dishes.",
        "home_details_title": "Luxury in the Details",
        "home_details_text": "We believe true luxury lives in detail — from handcrafted table settings and elegant plating, to personalized service that anticipates every guest’s desire. Every visit to Moscow Restaurant is not simply a dinner, but a carefully orchestrated experience.",
        "home_gallery_title": "Gallery",
        "home_gallery_alt": "Restaurant interior",

        # ===== BOOKING =====
        "booking_title": "Reserve Your Table",
        "booking_subtitle": "An evening of refinement begins with a reservation.",
        "booking_full_name": "Full Name",
        "booking_full_name_ph": "Your name",
        "booking_email": "Email",
        "booking_email_ph": "name@email.com",
        "booking_phone": "Phone",
        "booking_phone_ph": "+33 ...",
        "booking_date": "Date",
        "booking_time": "Time",
        "booking_time_placeholder": "Select time",
        "booking_guests": "Guests",
        "booking_guests_placeholder": "Number",
        "booking_occasion": "Occasion (optional)",
        "booking_occasion_ph": "Birthday, anniversary...",
        "booking_requests": "Special Requests (optional)",
        "booking_requests_ph": "Allergies, preferences, seating...",
        "booking_opt_caviar": "Caviar service upon arrival",
        "booking_opt_champagne": "Champagne on arrival",
        "booking_opt_private": "Private dining request",
        "booking_note": "For parties of 6 or more, card authorization may be requested. Cancellation policy: 24h notice.",
        "booking_submit": "Confirm Reservation",
        "booking_success": "Thank you for your reservation. We will contact you shortly to confirm your table.",
        "booking_side_title": "MOSCOW",
        "booking_side_sub": "Fine Russian Cuisine — Paris",

        # ===== MENU PAGE =====
        "menu_title": "Menu",
        "menu_signature": "Signature",
        "menu_intro": "Explore our signature dishes — caviar service, king crab, and refined Russian classics.",

        "menu_caviar": "Caviar",
        "menu_starters": "Starters",
        "menu_mains": "Main Courses",
        "menu_dessert": "Dessert",
        "menu_wine_spirits": "Wine & Spirits",

        "menu_champagne": "Champagne",
        "menu_white": "White Wines",
        "menu_red": "Red Wines",
        "menu_vodka": "Vodka",
        "menu_cocktails": "Signature Cocktails",

        "m_cav_1": "Beluga Caviar (30g)",
        "m_cav_2": "Oscietra Royal (30g)",
        "m_cav_3": "Sevruga Imperial (30g)",
        "m_cav_4": "Blinis & Traditional Garnish",
        "m_cav_5": "Caviar Tasting Trio (3×10g)",

        "m_s_1": "Kamchatka King Crab Salad",
        "m_s_2": "Beef Tartare “Moscow Style”",
        "m_s_3": "Salmon Gravlax",
        "m_s_4": "Russian Pickles & Forest Mushrooms",
        "m_s_5": "Borscht with Beef & Smoked Sour Cream",

        "m_m_1": "Beef Stroganoff (Prime Filet)",
        "m_m_2": "Siberian Pelmeni (Traditional)",
        "m_m_3": "Siberian Pelmeni (Truffle)",
        "m_m_4": "Black Cod with Caviar Sauce",
        "m_m_5": "Dry-Aged Ribeye (300g)",

        "m_d_1": "Medovik (Honey Cake)",
        "m_d_2": "Napoleon Mille-Feuille",
        "m_d_3": "Syrniki with Berry Coulis",
        "m_d_4": "Chocolate Fondant",
        "m_d_5": "Tea Ceremony (Selection)",

        "m_ch_1": "Moët & Chandon Brut Impérial",
        "m_ch_2": "Veuve Clicquot Yellow Label",
        "m_ch_3": "Ruinart Blanc de Blancs",
        "m_ch_4": "Dom Pérignon Vintage",
        "m_ch_5": "Cristal Louis Roederer",

        "m_w_1": "Chablis Premier Cru",
        "m_w_2": "Sancerre",
        "m_w_3": "Meursault",
        "m_w_4": "Riesling Grand Cru (Alsace)",
        "m_w_5": "Puligny-Montrachet",

        "m_r_1": "Bordeaux Grand Cru",
        "m_r_2": "Saint-Émilion Grand Cru",
        "m_r_3": "Barolo DOCG",
        "m_r_4": "Brunello di Montalcino",
        "m_r_5": "Châteauneuf-du-Pape",

        "m_v_1": "Beluga Noble",
        "m_v_2": "Beluga Gold Line",
        "m_v_3": "Stolichnaya Elit",
        "m_v_4": "Russian Standard Platinum",
        "m_v_5": "Imperial Collection Vodka",

        "m_c_1": "Imperial Moscow Mule",
        "m_c_2": "Russian Martini",
        "m_c_3": "Tsar’s Negroni",
        "m_c_4": "Black Pearl",
        "m_c_5": "Smoked Old Fashioned",

        # ===== NEWS PAGE =====
        "news_title": "News",
        "news_1_date": "15 February 2026",
        "news_1_title": "Michelin Star Award",
        "news_1_text": "We are honored to announce that Moscow Restaurant has been awarded its first Michelin Star. This distinction reflects our dedication to precision, craftsmanship, and the finest ingredients. From our caviar selection to our refined interpretation of Russian classics, every dish is created with discipline and passion. We extend our gratitude to our guests and our team who share our pursuit of excellence.",
        "news_1_alt": "Michelin Star",

        "news_2_date": "1 May 2026",
        "news_2_title": "Summer Terrace Opening",
        "news_2_text": "This spring, Moscow Restaurant unveils its elegant summer terrace in the heart of Paris. Designed as a discreet urban retreat, the terrace offers a refined open-air dining experience with curated champagne service and signature dishes. Reservations for terrace seating are now open.",
        "news_2_alt": "Summer Terrace",

        "news_3_date": "Limited Time Offer",
        "news_3_title": "Seasonal Promotions",
        "news_3_text": "For a limited time, we introduce: • Caviar & Champagne Pairing Experience • Chef’s Tasting Menu (7 courses) • Exclusive Weekday Lunch Menu. These seasonal offerings celebrate the finest flavors of the season in a more intimate format.",
        "news_3_alt": "Seasonal Promotions",

        # ===== RULES PAGE =====
        "rules_page_title": "Rules",
        "rules_headline": "Rules & Policies",
        "rules_intro": "At Moscow Restaurant, we are dedicated to creating an atmosphere of refined elegance, comfort, and discretion. To preserve the unique dining experience for all our guests, we kindly ask that the following guidelines be respected.",

        "rules_dress_title": "Dress Code",
        "rules_dress_p1": "We maintain a smart elegant dress code.",
        "rules_dress_p2": "Gentlemen are encouraged to wear tailored trousers, a shirt, and closed shoes. Jackets are appreciated for evening service. Sportswear, flip-flops, beachwear, and overly casual attire are not permitted.",
        "rules_dress_p3": "Ladies are invited to embrace elegant evening style.",
        "rules_dress_p4": "Our team reserves the right to refuse entry if the dress code is not respected.",

        "rules_reservations_title": "Reservations",
        "rules_reservations_p1": "We strongly recommend reservations, especially for dinner service and weekends.",
        "rules_reservations_p2": "For caviar service, tasting menus, or private dining, advance booking is required. Reservations may be secured online or by phone.",
        "rules_reservations_p3": "In order to guarantee your table, a card authorization may be requested for large parties.",

        "rules_cancel_title": "Cancellation Policy",
        "rules_cancel_p1": "Cancellations must be made at least 24 hours in advance.",
        "rules_cancel_p2": "Late cancellations or no-shows may result in a cancellation fee per guest.",

        "rules_timings_title": "Timings",
        "rules_lunch": "Lunch: 12:00 – 15:00",
        "rules_dinner": "Dinner: 18:30 – 23:30",
        "rules_timings_note": "Please arrive on time. We will hold your table for 15 minutes after the reserved time.",

        "rules_private_title": "Private Events",
        "rules_private_p1": "Private dining and exclusive events are available upon request.",
        "rules_private_p2": "For bespoke menus, wine pairings, or corporate evenings, please contact our reservations team.",

        "rules_children_title": "Children & Guests",
        "rules_children_p1": "Children are welcome during lunch service.",
        "rules_children_p2": "Evening service is recommended for guests aged 12 and above to maintain a calm and intimate ambiance.",

        "rules_photo_title": "Photography & Discretion",
        "rules_photo_p1": "Discreet photography is permitted. Professional filming requires prior approval.",
        "rules_photo_p2": "We kindly ask our guests to respect the privacy of others.",

        "rules_thanks_title": "Thank You",
        "rules_thanks_text": "We thank you for respecting these guidelines and look forward to welcoming you for an unforgettable culinary journey.",
    },

    "fr": {
        # ===== NAV =====
        "nav_menu": "Carte",
        "nav_rules": "Règlement",
        "nav_news": "Actualités",
        "nav_language": "Langue",

        # ===== HEADER LINKS =====
        "home_about": "À propos",
        "home_contacts": "Contacts",
        "home_booking": "Réserver",

        # ===== FOOTER =====
        "footer_contacts": "CONTACTS",

        # ===== HOME =====
        "home_title": "À propos de Moscow Restaurant",
        "home_philosophy_title": "Notre philosophie",
        "home_philosophy_text": "Moscow Restaurant est une destination gastronomique raffinée où la tradition rencontre l’art culinaire contemporain. Inspirés par la haute cuisine européenne et enrichis par l’héritage russe, nous créons des plats qui célèbrent la profondeur, la précision et l’émotion.",
        "home_craft_title": "Savoir-faire culinaire",
        "home_craft_text": "Notre philosophie repose sur une sélection exigeante de produits de saison, des saveurs équilibrées et une présentation irréprochable. Chaque assiette est pensée non seulement pour satisfaire, mais pour raconter une histoire — où chaque texture, chaque arôme et chaque détail fait partie de l’expérience.",
        "home_chef_title": "Rencontrez le Chef",
        "home_chef_text": "Au cœur de notre cuisine se tient le Chef Aleksandr Morozov — un artiste culinaire visionnaire formé dans des établissements étoilés Michelin à travers l’Europe. Son approche allie technique classique et créativité contemporaine, transformant chaque plat en une expérience sensorielle.",
        "home_beyond_text": "Au-delà de la cuisine, Moscow Restaurant offre une atmosphère de luxe discret : lumière chaleureuse, intérieur raffiné et cadre intime pensé pour des soirées inoubliables. Ici, le temps ralentit — et chaque dîner devient un moment à retenir.",
        "home_wine_title": "Une expérience œnologique sur mesure",
        "home_wine_text": "Notre carte des vins est élaborée avec la même exigence que notre cuisine. Entre millésimes rares et grandes maisons de France, d’Italie et d’Espagne, chaque sélection est choisie pour sublimer la dégustation et accompagner la richesse de nos plats.",
        "home_details_title": "Le luxe dans les détails",
        "home_details_text": "Nous croyons que le vrai luxe se cache dans les détails — de l’art de la table à la précision du dressage, jusqu’à un service personnalisé qui anticipe chaque désir. Chaque visite au Moscow Restaurant n’est pas simplement un dîner, mais une expérience soigneusement orchestrée.",
        "home_gallery_title": "Galerie",
        "home_gallery_alt": "Intérieur du restaurant",

        # ===== BOOKING =====
        "booking_title": "Réserver une table",
        "booking_subtitle": "Une soirée d’exception commence par une réservation.",
        "booking_full_name": "Nom complet",
        "booking_full_name_ph": "Votre nom",
        "booking_email": "E-mail",
        "booking_email_ph": "nom@email.com",
        "booking_phone": "Téléphone",
        "booking_phone_ph": "+33 ...",
        "booking_date": "Date",
        "booking_time": "Heure",
        "booking_time_placeholder": "Choisir une heure",
        "booking_guests": "Convives",
        "booking_guests_placeholder": "Nombre",
        "booking_occasion": "Occasion (optionnel)",
        "booking_occasion_ph": "Anniversaire, célébration…",
        "booking_requests": "Demandes spéciales (optionnel)",
        "booking_requests_ph": "Allergies, préférences, placement…",
        "booking_opt_caviar": "Service de caviar à l’arrivée",
        "booking_opt_champagne": "Champagne à l’arrivée",
        "booking_opt_private": "Demande de salon privé",
        "booking_note": "Pour les tables de 6 personnes ou plus, une autorisation de carte peut être demandée. Politique d’annulation : 24h.",
        "booking_submit": "Confirmer la réservation",
        "booking_success": "Merci pour votre réservation. Nous vous contacterons rapidement pour confirmer votre table.",
        "booking_side_title": "MOSCOW",
        "booking_side_sub": "Gastronomie russe — Paris",

        # ===== MENU PAGE =====
        "menu_title": "Carte",
        "menu_signature": "Signature",
        "menu_intro": "Découvrez nos plats signatures — service de caviar, crabe royal et grands classiques russes revisités.",

        "menu_caviar": "Caviar",
        "menu_starters": "Entrées",
        "menu_mains": "Plats principaux",
        "menu_dessert": "Desserts",
        "menu_wine_spirits": "Vins & spiritueux",

        "menu_champagne": "Champagne",
        "menu_white": "Vins blancs",
        "menu_red": "Vins rouges",
        "menu_vodka": "Vodka",
        "menu_cocktails": "Cocktails signature",

        "m_cav_1": "Caviar Beluga (30g)",
        "m_cav_2": "Oscietra Royal (30g)",
        "m_cav_3": "Sevruga Impérial (30g)",
        "m_cav_4": "Blinis & garnitures traditionnelles",
        "m_cav_5": "Trio dégustation de caviar (3×10g)",

        "m_s_1": "Salade de crabe royal du Kamtchatka",
        "m_s_2": "Tartare de bœuf « style Moscow »",
        "m_s_3": "Gravlax de saumon",
        "m_s_4": "Pickles russes & champignons des bois",
        "m_s_5": "Bortsch au bœuf & crème fumée",

        "m_m_1": "Bœuf Stroganoff (filet premium)",
        "m_m_2": "Pelmeni sibériens (traditionnels)",
        "m_m_3": "Pelmeni sibériens (truffe)",
        "m_m_4": "Morue noire, sauce au caviar",
        "m_m_5": "Ribeye maturé (300g)",

        "m_d_1": "Medovik (gâteau au miel)",
        "m_d_2": "Napoléon mille-feuille",
        "m_d_3": "Syrniki & coulis de fruits rouges",
        "m_d_4": "Fondant au chocolat",
        "m_d_5": "Cérémonie du thé (sélection)",

        "m_ch_1": "Moët & Chandon Brut Impérial",
        "m_ch_2": "Veuve Clicquot Yellow Label",
        "m_ch_3": "Ruinart Blanc de Blancs",
        "m_ch_4": "Dom Pérignon Vintage",
        "m_ch_5": "Cristal Louis Roederer",

        "m_w_1": "Chablis Premier Cru",
        "m_w_2": "Sancerre",
        "m_w_3": "Meursault",
        "m_w_4": "Riesling Grand Cru (Alsace)",
        "m_w_5": "Puligny-Montrachet",

        "m_r_1": "Bordeaux Grand Cru",
        "m_r_2": "Saint-Émilion Grand Cru",
        "m_r_3": "Barolo DOCG",
        "m_r_4": "Brunello di Montalcino",
        "m_r_5": "Châteauneuf-du-Pape",

        "m_v_1": "Beluga Noble",
        "m_v_2": "Beluga Gold Line",
        "m_v_3": "Stolichnaya Elit",
        "m_v_4": "Russian Standard Platinum",
        "m_v_5": "Vodka Imperial Collection",

        "m_c_1": "Imperial Moscow Mule",
        "m_c_2": "Martini russe",
        "m_c_3": "Negroni du Tsar",
        "m_c_4": "Perle noire",
        "m_c_5": "Old Fashioned fumé",

        # ===== NEWS PAGE =====
        "news_title": "Actualités",
        "news_1_date": "15 février 2026",
        "news_1_title": "Première étoile Michelin",
        "news_1_text": "Nous sommes honorés d’annoncer que Moscow Restaurant a obtenu sa première étoile Michelin. Cette distinction reflète notre exigence de précision, de savoir-faire et de produits d’exception. Du service de caviar à notre interprétation raffinée des classiques russes, chaque plat est créé avec discipline et passion. Merci à nos clients et à notre équipe, unis par la quête de l’excellence.",
        "news_1_alt": "Étoile Michelin",

        "news_2_date": "1er mai 2026",
        "news_2_title": "Ouverture de la terrasse d’été",
        "news_2_text": "Ce printemps, Moscow Restaurant dévoile son élégante terrasse d’été au cœur de Paris. Conçue comme un refuge urbain discret, elle propose une expérience gastronomique en plein air, accompagnée d’un service de champagne sélectionné et de plats signatures. Les réservations pour la terrasse sont ouvertes.",
        "news_2_alt": "Terrasse d’été",

        "news_3_date": "Offre limitée",
        "news_3_title": "Offres saisonnières",
        "news_3_text": "Pour une durée limitée, découvrez : • Accords caviar & champagne • Menu dégustation du Chef (7 services) • Menu déjeuner exclusif en semaine. Ces propositions célèbrent les plus belles saveurs de saison dans un format plus intime.",
        "news_3_alt": "Offres saisonnières",

        # ===== RULES PAGE =====
        "rules_page_title": "Règlement",
        "rules_headline": "Règles & Politique",
        "rules_intro": "Au Moscow Restaurant, nous tenons à créer une atmosphère d’élégance, de confort et de discrétion. Afin de préserver l’expérience pour tous nos invités, nous vous remercions de respecter les règles suivantes.",

        "rules_dress_title": "Code vestimentaire",
        "rules_dress_p1": "Nous appliquons un code vestimentaire chic et élégant.",
        "rules_dress_p2": "Messieurs : pantalon habillé, chemise et chaussures fermées. La veste est appréciée le soir. Les tenues de sport, tongs, tenues de plage et vêtements trop décontractés ne sont pas autorisés.",
        "rules_dress_p3": "Mesdames : une tenue de soirée élégante est encouragée.",
        "rules_dress_p4": "Notre équipe se réserve le droit de refuser l’entrée si le code vestimentaire n’est pas respecté.",

        "rules_reservations_title": "Réservations",
        "rules_reservations_p1": "Nous recommandons fortement de réserver, en particulier le soir et le week-end.",
        "rules_reservations_p2": "Pour le service de caviar, les menus dégustation ou un salon privé, une réservation à l’avance est requise. Réservation en ligne ou par téléphone.",
        "rules_reservations_p3": "Pour garantir votre table, une autorisation de carte peut être demandée pour les grands groupes.",

        "rules_cancel_title": "Politique d’annulation",
        "rules_cancel_p1": "Les annulations doivent être effectuées au moins 24 heures à l’avance.",
        "rules_cancel_p2": "Les annulations tardives ou les absences peuvent entraîner des frais par personne.",

        "rules_timings_title": "Horaires",
        "rules_lunch": "Déjeuner : 12h00 – 15h00",
        "rules_dinner": "Dîner : 18h30 – 23h30",
        "rules_timings_note": "Merci d’arriver à l’heure. Nous conservons votre table pendant 15 minutes après l’heure de réservation.",

        "rules_private_title": "Événements privés",
        "rules_private_p1": "Un salon privé et des événements exclusifs sont disponibles sur demande.",
        "rules_private_p2": "Pour des menus sur mesure, accords mets-vins ou soirées d’entreprise, contactez notre équipe de réservation.",

        "rules_children_title": "Enfants & invités",
        "rules_children_p1": "Les enfants sont les bienvenus au déjeuner.",
        "rules_children_p2": "Le service du soir est recommandé à partir de 12 ans afin de préserver une ambiance calme et intimiste.",

        "rules_photo_title": "Photographie & discrétion",
        "rules_photo_p1": "La photographie discrète est autorisée. Tout tournage professionnel nécessite une autorisation préalable.",
        "rules_photo_p2": "Nous vous remercions de respecter la vie privée des autres invités.",

        "rules_thanks_title": "Merci",
        "rules_thanks_text": "Merci de respecter ces règles. Nous serons ravis de vous accueillir pour une expérience culinaire inoubliable.",
    }
}


def get_lang() -> str:
    lang = request.cookies.get("lang", "en")
    return lang if lang in TRANSLATIONS else "en"


@app.context_processor
def inject_translations():
    lang = get_lang()
    return {"t": TRANSLATIONS[lang], "lang": lang}


# ===== ROUTES =====
@app.route("/")
def home():
    return render_template("index.html")


@app.route("/menu")
def menu():
    return render_template("menu.html")


@app.route("/booking")
def booking():
    return render_template("booking.html")


@app.route("/rules")
def rules():
    return render_template("rules.html")


@app.route("/news")
def news():
    return render_template("news.html")


@app.route("/set-lang/<lang_code>")
def set_lang(lang_code: str):
    if lang_code not in TRANSLATIONS:
        lang_code = "en"

    # IMPORTANT: your endpoint name is "home", not "index"
    next_url = request.referrer or url_for("home")

    resp = make_response(redirect(next_url))
    resp.set_cookie("lang", lang_code, max_age=60 * 60 * 24 * 365)
    return resp


if __name__ == "__main__":
    app.run(debug=True)
