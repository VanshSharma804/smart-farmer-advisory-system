import streamlit as st
import requests

language = st.selectbox(
    "Select Language",
    ["English", "हिंदी"]
)


if language == "English":
    st.markdown(
        '<h1 style="text-align:center; margin-bottom:5px;">Smart Farmer Advisory System</h1>',
        unsafe_allow_html=True
    )
    st.markdown(
        '<p style="text-align:center; color:#8f9992; font-size:16px; margin-bottom:25px;">Simple and useful farming guidance for better decisions</p>',
        unsafe_allow_html=True
    )
else:
    st.markdown(
        '<h1 style="text-align:center; margin-bottom:5px;">स्मार्ट किसान सलाह प्रणाली</h1>',
        unsafe_allow_html=True
    )
    st.markdown(
        '<p style="text-align:center; color:#8f9992; font-size:16px; margin-bottom:25px;">बेहतर खेती के लिए सरल और उपयोगी सलाह</p>',
        unsafe_allow_html=True
    )
    
st.markdown("""
<style>
.main-header {
    padding: 28px 10px 20px 10px;
    text-align: center;
}

.main-title {
    font-size: 38px;
    font-weight: 700;
    margin-bottom: 8px;
}

.main-subtitle {
    font-size: 16px;
    color: #9aa39d;
}
</style>
""", unsafe_allow_html=True)    
    
text = {
    "English": {
        "crop": "Crop Information",
        "irrigation": "Irrigation",
        "fertilizer": "Fertilizer",
        "weather": "Weather",
        "calendar": "Crop Calendar",
        "select_crop": "Select a crop",
        "description": "Get simple and useful farming guidance for crops, irrigation, fertilizer, weather and crop planning.",
        "start": "Select an option below to get started.",
        "services": "Farmer Services",
        "crop_desc": "View crop season, soil and water requirements.",
        "irrigation_desc": "Get irrigation advice based on soil moisture.",
        "fertilizer_desc": "Get fertilizer guidance for different crops.",
        "weather_desc": "Check temperature, humidity and rainfall.",
        "calendar_desc": "View sowing, growth and harvest information.",
        "season": "Growing Season",
        "water_requirement": "Water Requirement",
        "soil": "Suitable Soil",
        "temperature": "Suitable Temperature",
        "harvest": "Harvest Time",
        "tip": "Farming Tip",
        "explore": "Explore →",
        "pest": "Pest & Disease Detection",
        "pest_desc": "Identify common crop pests and diseases and get basic prevention guidance.",
        "pest_intro": "Select your crop to see common pests, diseases, symptoms and basic prevention.",
        "select_crop_pest": "Select Crop",
        "pest_result": "Pest & Disease Information",
        "yield_prediction": "Yield Prediction",
        "yield_desc": "Estimate crop yield using field and weather conditions.",
        "select_crop_yield": "Select Crop",
        "area": "Farm Area (hectares)",
        "temperature_yield": "Average Temperature (°C)",
        "rainfall_yield": "Rainfall (mm)",
        "soil_yield": "Select Soil Type",
        "fertilizer_yield": "Fertilizer Usage",
        "predict_yield": "Predict Yield",
        "yield_note": "This is an estimated value. Actual yield may vary depending on farming conditions.",
        
    },

    "हिंदी": {
        "crop": "फसल की जानकारी",
        "irrigation": "सिंचाई",
        "fertilizer": "उर्वरक",
        "weather": "मौसम",
        "calendar": "फसल कैलेंडर",
        "select_crop": "फसल चुनें",
        "description": "फसलों, सिंचाई, उर्वरक, मौसम और फसल योजना के लिए सरल और उपयोगी खेती की जानकारी प्राप्त करें।",
        "start": "शुरू करने के लिए नीचे एक विकल्प चुनें।",
        "services": "किसान सेवाएं",
        "crop_desc": "फसल के मौसम, मिट्टी और पानी की आवश्यकता देखें।",
        "irrigation_desc": "मिट्टी की नमी के आधार पर सिंचाई की सलाह प्राप्त करें।",
        "fertilizer_desc": "अलग-अलग फसलों के लिए उर्वरक की जानकारी प्राप्त करें।",
        "weather_desc": "तापमान, नमी और वर्षा की जानकारी देखें।",
        "calendar_desc": "बुवाई, विकास और कटाई की जानकारी देखें।",
        "season": "बढ़ने का मौसम",
        "water_requirement": "पानी की आवश्यकता",
        "soil": "उपयुक्त मिट्टी",
        "temperature": "उपयुक्त तापमान",
        "harvest": "कटाई का समय",
        "tip": "खेती की सलाह",
        "explore": "जानकारी देखें →",
        "pest": "कीट और रोग पहचान",
        "pest_desc": "सामान्य फसल कीट और रोगों की जानकारी तथा बचाव की सलाह प्राप्त करें।",
        "pest_intro": "अपनी फसल चुनें और सामान्य कीट, रोग, लक्षण और बचाव की जानकारी देखें।",
        "select_crop_pest": "फसल चुनें",
        "pest_result": "कीट और रोग की जानकारी",
        "yield_prediction": "उपज का अनुमान",
        "yield_desc": "खेत और मौसम की परिस्थितियों के आधार पर फसल की अनुमानित उपज जानें।",
        "select_crop_yield": "फसल चुनें",
        "area": "खेत का क्षेत्रफल (हेक्टेयर)",
        "temperature_yield": "औसत तापमान (°C)",
        "rainfall_yield": "वर्षा (mm)",
        "soil_yield": "मिट्टी का प्रकार चुनें",
        "fertilizer_yield": "उर्वरक का उपयोग",
        "predict_yield": "उपज का अनुमान लगाएं",
        "yield_note": "यह एक अनुमानित मान है। वास्तविक उपज खेती की परिस्थितियों के अनुसार अलग हो सकती है।",
        
    }
}    

if "selected_option" not in st.session_state:
    st.session_state["selected_option"] = None

option = st.session_state["selected_option"]

if option is None:

    st.write(text[language]["description"])
    st.info(text[language]["start"])
    st.header(text[language]["services"])

    st.markdown("""
    <style>
    .service-card {
        background: linear-gradient(145deg, #18251d, #101713);
        border: 1px solid #34483a;
        border-radius: 18px;
        padding: 18px;
        margin-bottom: 6px;
        min-height: 175px;
        transition: all 0.25s ease;
    }

    .service-card:hover {
        transform: translateY(-3px);
        border-color: #5f8068;
        box-shadow: 0 7px 18px rgba(0, 0, 0, 0.25);
    }

    .service-image {
        height: 82px;
        background: linear-gradient(145deg, #263b2d, #17231c);
        border-radius: 13px;
        display: flex;
        align-items: center;
        justify-content: center;
        font-size: 45px;
        margin-bottom: 14px;
        border: 1px solid #3b5141;
    }

    .service-title {
        font-size: 20px;
        font-weight: 700;
        margin-bottom: 5px;
    }

    .service-description {
        color: #b5b9b6;
        font-size: 13px;
        line-height: 1.45;
        min-height: 40px;
    }

    div.stButton > button {
        width: 100%;
        border-radius: 10px;
        border: 1px solid #4d6755;
        background: #1d2d23;
        color: white;
        font-size: 14px;
        font-weight: 600;
        padding: 9px 14px;
        transition: all 0.2s ease;
    }

    div.stButton > button:hover {
        background: #29402f;
        border-color: #6b8d74;
        transform: translateY(-1px);
    }

    .hero-box {
        background: linear-gradient(145deg, #18251d, #101713);
        border: 1px solid #34483a;
        border-radius: 22px;
        padding: 35px;
        text-align: center;
        margin-bottom: 25px;
    }

    .hero-icon {
        font-size: 75px;
        margin-bottom: 10px;
    }

    .hero-title {
        font-size: 30px;
        font-weight: 700;
    }

    .hero-description {
        color: #b5b9b6;
        font-size: 16px;
        margin-top: 8px;
    }
    
    @media (max-width: 768px) {

    .service-card {
        padding: 16px;
        min-height: 165px;
        margin-bottom: 5px;
    }

    .service-image {
        height: 75px;
        font-size: 40px;
        margin-bottom: 12px;
    }

    .service-title {
        font-size: 18px;
    }

    .service-description {
        font-size: 13px;
        min-height: 35px;
    }

    .hero-box {
        padding: 25px 18px;
        margin-bottom: 20px;
    }

    .hero-icon {
        font-size: 60px;
    }

    .hero-title {
        font-size: 25px;
    }

    .hero-description {
        font-size: 14px;
    }
   }  
    </style>
    """, unsafe_allow_html=True)

    col1, col2 = st.columns(2)

    with col1:
        st.markdown("""
        <div class="service-card">
            <div class="service-image">🌾</div>
            <div class="service-title">""" + text[language]["crop"] + """</div>
            <div class="service-description">
                """ + text[language]["crop_desc"] + """
            </div>
        </div>
        """, unsafe_allow_html=True)

        if st.button(text[language]["explore"], key="crop_card", use_container_width=True):
            st.session_state["selected_option"] = "Crop Information"
            st.rerun()

    with col2:
        st.markdown("""
        <div class="service-card">
            <div class="service-image">💧</div>
            <div class="service-title">""" + text[language]["irrigation"] + """</div>
            <div class="service-description">
                """ + text[language]["irrigation_desc"] + """
            </div>
        </div>
        """, unsafe_allow_html=True)

        if st.button(text[language]["explore"], key="irrigation_card", use_container_width=True):
            st.session_state["selected_option"] = "Irrigation"
            st.rerun()

    col3, col4 = st.columns(2)

    with col3:
        st.markdown("""
        <div class="service-card">
            <div class="service-image">🧪</div>
            <div class="service-title">""" + text[language]["fertilizer"] + """</div>
            <div class="service-description">
                """ + text[language]["fertilizer_desc"] + """
            </div>
        </div>
        """, unsafe_allow_html=True)

        if st.button(text[language]["explore"], key="fertilizer_card", use_container_width=True):
            st.session_state["selected_option"] = "Fertilizer"
            st.rerun()

    with col4:
        st.markdown("""
        <div class="service-card">
            <div class="service-image">🌦️</div>
            <div class="service-title">""" + text[language]["weather"] + """</div>
            <div class="service-description">
                """ + text[language]["weather_desc"] + """
            </div>
        </div>
        """, unsafe_allow_html=True)

        if st.button(text[language]["explore"], key="weather_card", use_container_width=True):
            st.session_state["selected_option"] = "Weather"
            st.rerun()

    col5, col6 = st.columns(2)

    with col5:
        st.markdown("""
        <div class="service-card">
            <div class="service-image">📅</div>
            <div class="service-title">""" + text[language]["calendar"] + """</div>
            <div class="service-description">
                """ + text[language]["calendar_desc"] + """
            </div>
        </div>
        """, unsafe_allow_html=True)

        if st.button(text[language]["explore"], key="calendar_card", use_container_width=True):
            st.session_state["selected_option"] = "Crop Calendar"
            st.rerun()

    with col6:
        st.markdown("""
        <div class="service-card">
            <div class="service-image">🐛</div>
            <div class="service-title">""" + text[language]["pest"] + """</div>
            <div class="service-description">
                """ + text[language]["pest_desc"] + """
            </div>
        </div>
        """, unsafe_allow_html=True)

        if st.button(text[language]["explore"], key="pest_card", use_container_width=True):
            st.session_state["selected_option"] = "Pest & Disease Detection"
            st.rerun()

    col7, col8 = st.columns(2)

    with col7:
        st.markdown("""
        <div class="service-card">
            <div class="service-image">📊</div>
            <div class="service-title">""" + text[language]["yield_prediction"] + """</div>
            <div class="service-description">
                """ + text[language]["yield_desc"] + """
            </div>
        </div>
        """, unsafe_allow_html=True)

        if st.button(text[language]["explore"], key="yield_card", use_container_width=True):
            st.session_state["selected_option"] = "Yield Prediction"
            st.rerun()

else:

    if language == "English":
        back_text = "← Back to Dashboard"
    else:
        back_text = "← डैशबोर्ड पर वापस जाएं"

    if st.button(back_text, key="back_dashboard", use_container_width=False):
        st.session_state["selected_option"] = None
        st.rerun()

    feature_visuals = {
        "Crop Information": "🌾",
        "Irrigation": "💧",
        "Fertilizer": "🧪",
        "Weather": "🌦️",
        "Crop Calendar": "📅",
        "Pest & Disease Detection": "🐛",
        "Yield Prediction": "📊"
    }

    feature_descriptions = {
        "Crop Information": text[language]["crop_desc"],
        "Irrigation": text[language]["irrigation_desc"],
        "Fertilizer": text[language]["fertilizer_desc"],
        "Weather": text[language]["weather_desc"],
        "Crop Calendar": text[language]["calendar_desc"],
        "Pest & Disease Detection": text[language]["pest_desc"],
        "Yield Prediction": text[language]["yield_desc"]
    }

    feature_titles = {
        "Crop Information": text[language]["crop"],
        "Irrigation": text[language]["irrigation"],
        "Fertilizer": text[language]["fertilizer"],
        "Weather": text[language]["weather"],
        "Crop Calendar": text[language]["calendar"],
        "Pest & Disease Detection": text[language]["pest"],
        "Yield Prediction": text[language]["yield_prediction"]
    }

    st.markdown("""
    <style>
    .feature-header {
        background: linear-gradient(145deg, #18251d, #101713);
        border: 1px solid #34483a;
        border-radius: 20px;
        padding: 28px 30px;
        margin: 20px 0 30px 0;
    }

    .feature-header-icon {
        font-size: 52px;
        margin-bottom: 8px;
    }

    .feature-header-title {
        font-size: 32px;
        font-weight: 700;
        margin-bottom: 8px;
    }

    .feature-header-description {
        color: #b5b9b6;
        font-size: 15px;
        line-height: 1.6;
    }
    </style>

    <div class="feature-header">
        <div class="feature-header-icon">""" + feature_visuals[option] + """</div>
        <div class="feature-header-title">""" + feature_titles[option] + """</div>
        <div class="feature-header-description">""" + feature_descriptions[option] + """</div>
    </div>
    """, unsafe_allow_html=True)

crop_data = {
    "Wheat": {
        "name": {
            "English": "Wheat",
            "हिंदी": "गेहूं"
        },
        "season": {
            "English": "October - December",
            "हिंदी": "अक्टूबर - दिसंबर"
        },
        "water": {
            "English": "Moderate",
            "हिंदी": "मध्यम"
        },
        "soil": {
            "English": "Loamy soil",
            "हिंदी": "दोमट मिट्टी"
        },
        "temperature": {
            "English": "15°C - 25°C",
            "हिंदी": "15°C - 25°C"
        },
        "harvest": {
            "English": "March - April",
            "हिंदी": "मार्च - अप्रैल"
        },
        "tip": {
            "English": "Avoid excessive irrigation.",
            "हिंदी": "अधिक सिंचाई से बचें।"
        }
    },

    "Rice": {
        "name": {
            "English": "Rice",
            "हिंदी": "चावल"
        },
        "season": {
            "English": "June - July",
            "हिंदी": "जून - जुलाई"
        },
        "water": {
            "English": "High",
            "हिंदी": "अधिक"
        },
        "soil": {
            "English": "Clayey soil",
            "हिंदी": "चिकनी मिट्टी"
        },
        "temperature": {
            "English": "20°C - 35°C",
            "हिंदी": "20°C - 35°C"
        },
        "harvest": {
            "English": "October - November",
            "हिंदी": "अक्टूबर - नवंबर"
        },
        "tip": {
            "English": "Maintain proper water levels in the field.",
            "हिंदी": "खेत में पानी का उचित स्तर बनाए रखें।"
        }
    },

    "Potato": {
        "name": {
            "English": "Potato",
            "हिंदी": "आलू"
        },
        "season": {
            "English": "October - November",
            "हिंदी": "अक्टूबर - नवंबर"
        },
        "water": {
            "English": "Moderate",
            "हिंदी": "मध्यम"
        },
        "soil": {
            "English": "Loamy soil",
            "हिंदी": "दोमट मिट्टी"
        },
        "temperature": {
            "English": "15°C - 25°C",
            "हिंदी": "15°C - 25°C"
        },
        "harvest": {
            "English": "January - February",
            "हिंदी": "जनवरी - फरवरी"
        },
        "tip": {
            "English": "Avoid waterlogging in the soil.",
            "हिंदी": "मिट्टी में जलभराव से बचें।"
        }
    },

    "Maize": {
        "name": {
            "English": "Maize",
            "हिंदी": "मक्का"
        },
        "season": {
            "English": "June - July",
            "हिंदी": "जून - जुलाई"
        },
        "water": {
            "English": "Moderate",
            "हिंदी": "मध्यम"
        },
        "soil": {
            "English": "Loamy soil",
            "हिंदी": "दोमट मिट्टी"
        },
        "temperature": {
            "English": "18°C - 27°C",
            "हिंदी": "18°C - 27°C"
        },
        "harvest": {
            "English": "September - October",
            "हिंदी": "सितंबर - अक्टूबर"
        },
        "tip": {
            "English": "Avoid waterlogging and maintain proper soil moisture.",
            "हिंदी": "जलभराव से बचें और मिट्टी में उचित नमी बनाए रखें।"
        }
    },

    "Chana": {
        "name": {
            "English": "Chana",
            "हिंदी": "चना"
        },
        "season": {
            "English": "October - November",
            "हिंदी": "अक्टूबर - नवंबर"
        },
        "water": {
            "English": "Low",
            "हिंदी": "कम"
        },
        "soil": {
            "English": "Well-drained loamy soil",
            "हिंदी": "अच्छी जल निकासी वाली दोमट मिट्टी"
        },
        "temperature": {
            "English": "20°C - 25°C",
            "हिंदी": "20°C - 25°C"
        },
        "harvest": {
            "English": "February - March",
            "हिंदी": "फरवरी - मार्च"
        },
        "tip": {
            "English": "Avoid excessive irrigation.",
            "हिंदी": "अधिक सिंचाई से बचें।"
        }
    },

    "Mustard": {
        "name": {
            "English": "Mustard",
            "हिंदी": "सरसों"
        },
        "season": {
            "English": "October - November",
            "हिंदी": "अक्टूबर - नवंबर"
        },
        "water": {
            "English": "Low to Moderate",
            "हिंदी": "कम से मध्यम"
        },
        "soil": {
            "English": "Loamy soil",
            "हिंदी": "दोमट मिट्टी"
        },
        "temperature": {
            "English": "10°C - 25°C",
            "हिंदी": "10°C - 25°C"
        },
        "harvest": {
            "English": "February - March",
            "हिंदी": "फरवरी - मार्च"
        },
        "tip": {
            "English": "Avoid excessive watering during flowering.",
            "हिंदी": "फूल आने के समय अधिक पानी देने से बचें।"
        }
    },
    "Sugarcane": {
        "name": {"English": "Sugarcane", "हिंदी": "गन्ना"},
        "season": {"English": "February - March", "हिंदी": "फरवरी - मार्च"},
        "water": {"English": "High", "हिंदी": "अधिक"},
        "soil": {"English": "Deep fertile loamy soil", "हिंदी": "गहरी उपजाऊ दोमट मिट्टी"},
        "temperature": {"English": "20 - 35°C", "हिंदी": "20 - 35°C"},
        "harvest": {"English": "10 - 18 months", "हिंदी": "10 - 18 महीने"},
        "tip": {"English": "Maintain regular irrigation.", "हिंदी": "नियमित सिंचाई बनाए रखें।"}
    },

    "Tomato": {
        "name": {"English": "Tomato", "हिंदी": "टमाटर"},
        "season": {"English": "September - February", "हिंदी": "सितंबर - फरवरी"},
        "water": {"English": "Moderate", "हिंदी": "मध्यम"},
        "soil": {"English": "Well-drained loamy soil", "हिंदी": "अच्छी जल निकासी वाली दोमट मिट्टी"},
        "temperature": {"English": "18 - 27°C", "हिंदी": "18 - 27°C"},
        "harvest": {"English": "60 - 90 days", "हिंदी": "60 - 90 दिन"},
        "tip": {"English": "Avoid irregular irrigation.", "हिंदी": "अनियमित सिंचाई से बचें।"}
    },

    "Onion": {
        "name": {"English": "Onion", "हिंदी": "प्याज"},
        "season": {"English": "October - April", "हिंदी": "अक्टूबर - अप्रैल"},
        "water": {"English": "Moderate", "हिंदी": "मध्यम"},
        "soil": {"English": "Sandy loam soil", "हिंदी": "बलुई दोमट मिट्टी"},
        "temperature": {"English": "13 - 25°C", "हिंदी": "13 - 25°C"},
        "harvest": {"English": "March - April", "हिंदी": "मार्च - अप्रैल"},
        "tip": {"English": "Reduce irrigation before harvest.", "हिंदी": "कटाई से पहले सिंचाई कम करें।"}
    },

    "Carrot": {
        "name": {"English": "Carrot", "हिंदी": "गाजर"},
        "season": {"English": "October - February", "हिंदी": "अक्टूबर - फरवरी"},
        "water": {"English": "Moderate", "हिंदी": "मध्यम"},
        "soil": {"English": "Loose sandy loam soil", "हिंदी": "ढीली बलुई दोमट मिट्टी"},
        "temperature": {"English": "15 - 25°C", "हिंदी": "15 - 25°C"},
        "harvest": {"English": "70 - 100 days", "हिंदी": "70 - 100 दिन"},
        "tip": {"English": "Keep soil evenly moist.", "हिंदी": "मिट्टी में समान नमी रखें।"}
    },

    "Bottle Gourd": {
        "name": {"English": "Bottle Gourd", "हिंदी": "लौकी"},
        "season": {"English": "February - September", "हिंदी": "फरवरी - सितंबर"},
        "water": {"English": "Moderate to High", "हिंदी": "मध्यम से अधिक"},
        "soil": {"English": "Well-drained loamy soil", "हिंदी": "अच्छी जल निकासी वाली दोमट मिट्टी"},
        "temperature": {"English": "25 - 35°C", "हिंदी": "25 - 35°C"},
        "harvest": {"English": "60 - 90 days", "हिंदी": "60 - 90 दिन"},
        "tip": {"English": "Provide support to vines.", "हिंदी": "बेलों को सहारा दें।"}
    },

    "Cauliflower": {
        "name": {"English": "Cauliflower", "हिंदी": "फूलगोभी"},
        "season": {"English": "September - February", "हिंदी": "सितंबर - फरवरी"},
        "water": {"English": "Moderate", "हिंदी": "मध्यम"},
        "soil": {"English": "Fertile loamy soil", "हिंदी": "उपजाऊ दोमट मिट्टी"},
        "temperature": {"English": "15 - 25°C", "हिंदी": "15 - 25°C"},
        "harvest": {"English": "60 - 100 days", "हिंदी": "60 - 100 दिन"},
        "tip": {"English": "Maintain consistent soil moisture.", "हिंदी": "मिट्टी में लगातार नमी बनाए रखें।"}
    },

    "Cabbage": {
        "name": {"English": "Cabbage", "हिंदी": "पत्तागोभी"},
        "season": {"English": "September - February", "हिंदी": "सितंबर - फरवरी"},
        "water": {"English": "Moderate", "हिंदी": "मध्यम"},
        "soil": {"English": "Fertile loamy soil", "हिंदी": "उपजाऊ दोमट मिट्टी"},
        "temperature": {"English": "15 - 25°C", "हिंदी": "15 - 25°C"},
        "harvest": {"English": "70 - 120 days", "हिंदी": "70 - 120 दिन"},
        "tip": {"English": "Maintain regular irrigation.", "हिंदी": "नियमित सिंचाई बनाए रखें।"}
    },

    "Brinjal": {
        "name": {"English": "Brinjal", "हिंदी": "बैंगन"},
        "season": {"English": "Throughout the year in suitable conditions", "हिंदी": "उपयुक्त परिस्थितियों में पूरे वर्ष"},
        "water": {"English": "Moderate", "हिंदी": "मध्यम"},
        "soil": {"English": "Sandy loam soil", "हिंदी": "बलुई दोमट मिट्टी"},
        "temperature": {"English": "22 - 30°C", "हिंदी": "22 - 30°C"},
        "harvest": {"English": "60 - 90 days", "हिंदी": "60 - 90 दिन"},
        "tip": {"English": "Monitor plants for pests.", "हिंदी": "पौधों में कीटों की निगरानी करें।"}
    },

    "Okra": {
        "name": {"English": "Okra", "हिंदी": "भिंडी"},
        "season": {"English": "February - September", "हिंदी": "फरवरी - सितंबर"},
        "water": {"English": "Moderate", "हिंदी": "मध्यम"},
        "soil": {"English": "Well-drained loamy soil", "हिंदी": "अच्छी जल निकासी वाली दोमट मिट्टी"},
        "temperature": {"English": "24 - 32°C", "हिंदी": "24 - 32°C"},
        "harvest": {"English": "45 - 60 days", "हिंदी": "45 - 60 दिन"},
        "tip": {"English": "Harvest tender pods regularly.", "हिंदी": "कोमल फलियों की नियमित कटाई करें।"}
    },

    "Peas": {
        "name": {"English": "Peas", "हिंदी": "मटर"},
        "season": {"English": "October - February", "हिंदी": "अक्टूबर - फरवरी"},
        "water": {"English": "Moderate", "हिंदी": "मध्यम"},
        "soil": {"English": "Well-drained loamy soil", "हिंदी": "अच्छी जल निकासी वाली दोमट मिट्टी"},
        "temperature": {"English": "10 - 25°C", "हिंदी": "10 - 25°C"},
        "harvest": {"English": "60 - 90 days", "हिंदी": "60 - 90 दिन"},
        "tip": {"English": "Avoid waterlogging.", "हिंदी": "जलभराव से बचें।"}
    },

    "Cotton": {
        "name": {"English": "Cotton", "हिंदी": "कपास"},
        "season": {"English": "April - December", "हिंदी": "अप्रैल - दिसंबर"},
        "water": {"English": "Moderate", "हिंदी": "मध्यम"},
        "soil": {"English": "Black cotton soil", "हिंदी": "काली कपास मिट्टी"},
        "temperature": {"English": "21 - 30°C", "हिंदी": "21 - 30°C"},
        "harvest": {"English": "October - January", "हिंदी": "अक्टूबर - जनवरी"},
        "tip": {"English": "Monitor pests and avoid excess irrigation.", "हिंदी": "कीटों की निगरानी करें और अधिक सिंचाई से बचें।"}
    },

    "Bajra": {
        "name": {"English": "Bajra", "हिंदी": "बाजरा"},
        "season": {"English": "June - September", "हिंदी": "जून - सितंबर"},
        "water": {"English": "Low", "हिंदी": "कम"},
        "soil": {"English": "Sandy loam soil", "हिंदी": "बलुई दोमट मिट्टी"},
        "temperature": {"English": "25 - 35°C", "हिंदी": "25 - 35°C"},
        "harvest": {"English": "September - October", "हिंदी": "सितंबर - अक्टूबर"},
        "tip": {"English": "Bajra is relatively drought tolerant.", "हिंदी": "बाजरा सूखे को अपेक्षाकृत अच्छी तरह सहन करता है।"}
    },

    "Groundnut": {
        "name": {"English": "Groundnut", "हिंदी": "मूंगफली"},
        "season": {"English": "June - October", "हिंदी": "जून - अक्टूबर"},
        "water": {"English": "Moderate", "हिंदी": "मध्यम"},
        "soil": {"English": "Sandy loam soil", "हिंदी": "बलुई दोमट मिट्टी"},
        "temperature": {"English": "25 - 30°C", "हिंदी": "25 - 30°C"},
        "harvest": {"English": "September - October", "हिंदी": "सितंबर - अक्टूबर"},
        "tip": {"English": "Avoid waterlogging during pod development.", "हिंदी": "फली विकास के दौरान जलभराव से बचें।"}
    },

    "Soybean": {
        "name": {"English": "Soybean", "हिंदी": "सोयाबीन"},
        "season": {"English": "June - October", "हिंदी": "जून - अक्टूबर"},
        "water": {"English": "Moderate", "हिंदी": "मध्यम"},
        "soil": {"English": "Well-drained loamy soil", "हिंदी": "अच्छी जल निकासी वाली दोमट मिट्टी"},
        "temperature": {"English": "20 - 30°C", "हिंदी": "20 - 30°C"},
        "harvest": {"English": "September - October", "हिंदी": "सितंबर - अक्टूबर"},
        "tip": {"English": "Avoid prolonged waterlogging.", "हिंदी": "लंबे समय तक जलभराव से बचें।"}
    }
  }


def show_crop_information():
    
    st.subheader(text[language]["crop"])

    crop_names = {
        crop_data["Wheat"]["name"][language]: "Wheat",
        crop_data["Rice"]["name"][language]: "Rice",
        crop_data["Potato"]["name"][language]: "Potato",
        crop_data["Maize"]["name"][language]: "Maize",
        crop_data["Chana"]["name"][language]: "Chana",
        crop_data["Mustard"]["name"][language]: "Mustard",
        crop_data["Sugarcane"]["name"][language]: "Sugarcane",
        crop_data["Tomato"]["name"][language]: "Tomato",
        crop_data["Onion"]["name"][language]: "Onion",
        crop_data["Carrot"]["name"][language]: "Carrot",
        crop_data["Bottle Gourd"]["name"][language]: "Bottle Gourd",
        crop_data["Cauliflower"]["name"][language]: "Cauliflower",
        crop_data["Cabbage"]["name"][language]: "Cabbage",
        crop_data["Brinjal"]["name"][language]: "Brinjal",
        crop_data["Okra"]["name"][language]: "Okra",
        crop_data["Peas"]["name"][language]: "Peas",
        crop_data["Cotton"]["name"][language]: "Cotton",
        crop_data["Bajra"]["name"][language]: "Bajra",
        crop_data["Groundnut"]["name"][language]: "Groundnut",
        crop_data["Soybean"]["name"][language]: "Soybean"
    }

    selected_crop = st.selectbox(
        text[language]["select_crop"],
        list(crop_names.keys())
    )

    crop = crop_names[selected_crop]

    st.title(crop_data[crop]["name"][language])

    st.info(
        "This section gives simple basic information to help you understand "
        "the selected crop."
        if language == "English"
        else
        "यह जानकारी चुनी गई फसल को आसानी से समझने में आपकी मदद करेगी।"
    )

    col1, col2 = st.columns(2)

    with col1:
        st.markdown("### " + text[language]["season"])
        st.write(crop_data[crop]["season"][language])

        st.markdown("### " + text[language]["water_requirement"])
        st.write(crop_data[crop]["water"][language])

        st.markdown("### " + text[language]["soil"])
        st.write(crop_data[crop]["soil"][language])

    with col2:
        st.markdown("### " + text[language]["temperature"])
        st.write(crop_data[crop]["temperature"][language])

        st.markdown("### " + text[language]["harvest"])
        st.write(crop_data[crop]["harvest"][language])

        st.markdown("### " + text[language]["tip"])
        st.write(crop_data[crop]["tip"][language])

    st.divider()

    guide_title = {
    "English": "Simple Farmer Guide",
    "हिंदी": "किसान के लिए आसान जानकारी"
    }

    guide_text = {
        "English": [
            "Use this information as a basic guide for planning your crop.",
            "• Choose the right season for sowing.",
            "• Keep the soil suitable for the crop.",
            "• Give water according to the crop's requirement.",
            "• Monitor the crop regularly during growth.",
            "• Follow local agricultural advice when needed."
        ],
        "हिंदी": [
            "इस जानकारी का उपयोग फसल की योजना बनाने के लिए एक सामान्य मार्गदर्शक के रूप में करें।",
            "• बुवाई के लिए सही मौसम चुनें।",
            "• फसल के अनुसार उपयुक्त मिट्टी रखें।",
            "• फसल की जरूरत के अनुसार पानी दें।",
            "• फसल की बढ़वार के दौरान नियमित निगरानी करें।",
            "• जरूरत पड़ने पर स्थानीय कृषि विशेषज्ञ की सलाह लें।"
        ]
    }

    st.subheader(guide_title[language])

    for point in guide_text[language]:
        st.write(point)

if option == "Crop Information":
    show_crop_information()
    
    
def show_irrigation():
    
    if language == "English":
        heading = "Irrigation Advisory"
        crop_label = "Select Crop"
        moisture_label = "How does the soil look?"
        dry_option = "Dry"
        normal_option = "Normal"
        wet_option = "Wet"

        condition_title = "Current Field Condition"
        advice_title = "What should you do?"

        dry_description = (
            "The soil looks dry. The crop may not be getting enough water."
        )

        normal_description = (
            "The soil has a reasonable amount of moisture."
        )

        wet_description = (
            "The soil is already wet. Extra irrigation may not be needed."
        )

    else:
        heading = "सिंचाई की सलाह"
        crop_label = "फसल चुनें"
        moisture_label = "मिट्टी कैसी दिख रही है?"
        dry_option = "सूखी"
        normal_option = "सामान्य"
        wet_option = "गीली"

        condition_title = "खेत की वर्तमान स्थिति"
        advice_title = "आपको क्या करना चाहिए?"

        dry_description = (
            "मिट्टी सूखी लग रही है। फसल को पर्याप्त पानी नहीं मिल रहा हो सकता है।"
        )

        normal_description = (
            "मिट्टी में पर्याप्त मात्रा में नमी है।"
        )

        wet_description = (
            "मिट्टी पहले से गीली है। अभी अतिरिक्त सिंचाई की जरूरत नहीं हो सकती।"
        )

    st.subheader(heading)

    

    crop_names = {
        crop_data["Wheat"]["name"][language]: "Wheat",
        crop_data["Rice"]["name"][language]: "Rice",
        crop_data["Potato"]["name"][language]: "Potato",
        crop_data["Maize"]["name"][language]: "Maize",
        crop_data["Chana"]["name"][language]: "Chana",
        crop_data["Mustard"]["name"][language]: "Mustard",
        crop_data["Sugarcane"]["name"][language]: "Sugarcane",
        crop_data["Tomato"]["name"][language]: "Tomato",
        crop_data["Onion"]["name"][language]: "Onion",
        crop_data["Carrot"]["name"][language]: "Carrot",
        crop_data["Bottle Gourd"]["name"][language]: "Bottle Gourd",
        crop_data["Cauliflower"]["name"][language]: "Cauliflower",
        crop_data["Cabbage"]["name"][language]: "Cabbage",
        crop_data["Brinjal"]["name"][language]: "Brinjal",
        crop_data["Okra"]["name"][language]: "Okra",
        crop_data["Peas"]["name"][language]: "Peas",
        crop_data["Cotton"]["name"][language]: "Cotton",
        crop_data["Bajra"]["name"][language]: "Bajra",
        crop_data["Groundnut"]["name"][language]: "Groundnut",
        crop_data["Soybean"]["name"][language]: "Soybean"
    }

    selected_crop = st.selectbox(
        crop_label,
        list(crop_names.keys())
    )

    crop = crop_names[selected_crop]

    

    soil_condition = st.radio(
        moisture_label,
        [
            dry_option,
            normal_option,
            wet_option
        ],
        horizontal=True
    )

    
    st.subheader(condition_title)

    if soil_condition == dry_option:
        st.warning(dry_description)

    elif soil_condition == normal_option:
        st.info(normal_description)

    else:
        st.success(wet_description)

   
    if language == "English":

        crop_advice = {
            "Rice": {
                "dry": "Rice needs regular water. Irrigate the field according to the crop stage and local farming practice.",
                "normal": "Moisture is currently reasonable. Avoid unnecessary irrigation.",
                "wet": "Do not add extra water. Check for excessive standing water and drainage."
            },

            "Sugarcane": {
                "dry": "Sugarcane needs regular moisture. Irrigate if the soil is dry.",
                "normal": "Soil moisture is reasonable. Continue regular monitoring.",
                "wet": "Avoid extra irrigation and check that water is draining properly."
            },

            "Wheat": {
                "dry": "Irrigation may be needed. Check the soil around the root zone before watering.",
                "normal": "Moisture is suitable. Irrigate only when the crop needs water.",
                "wet": "Avoid irrigation now. Too much water can harm the crop."
            },

            "Potato": {
                "dry": "Potato needs consistent moisture. Irrigate if the soil is dry.",
                "normal": "Moisture is suitable. Maintain regular monitoring.",
                "wet": "Avoid extra irrigation because excess water can affect the roots and tubers."
            },

            "Maize": {
                "dry": "Irrigation may be needed. Pay special attention during important crop growth stages.",
                "normal": "Moisture is reasonable. Continue checking the soil.",
                "wet": "Avoid extra irrigation and check for waterlogging."
            },

            "Chana": {
                "dry": "If the soil is dry, irrigation may be needed. Avoid excessive watering.",
                "normal": "Moisture is reasonable. Continue monitoring the crop.",
                "wet": "Do not irrigate now. Avoid waterlogging."
            },

            "Mustard": {
                "dry": "Irrigation may be needed if the soil is dry, especially during important growth stages.",
                "normal": "Moisture is reasonable. Avoid unnecessary irrigation.",
                "wet": "Avoid irrigation and check field drainage."
            },

            "Tomato": {
                "dry": "Tomato needs regular moisture. Irrigate if the soil is dry.",
                "normal": "Moisture is suitable. Maintain regular watering when needed.",
                "wet": "Avoid extra irrigation because too much water can increase disease problems."
            },

            "Onion": {
                "dry": "Irrigation may be needed. Keep soil moisture reasonably even.",
                "normal": "Moisture is suitable. Continue monitoring.",
                "wet": "Avoid irrigation and allow excess water to drain."
            },

            "Carrot": {
                "dry": "Irrigation may be needed. Keep the soil evenly moist for good root development.",
                "normal": "Moisture is suitable. Continue regular monitoring.",
                "wet": "Avoid excess water because waterlogging can affect roots."
            },

            "Bottle Gourd": {
                "dry": "Irrigation may be needed because bottle gourd needs regular moisture.",
                "normal": "Moisture is reasonable. Continue monitoring.",
                "wet": "Avoid extra irrigation and check drainage."
            },

            "Cauliflower": {
                "dry": "Irrigation may be needed. Maintain regular soil moisture.",
                "normal": "Moisture is suitable. Continue monitoring.",
                "wet": "Avoid extra irrigation and check for waterlogging."
            },

            "Cabbage": {
                "dry": "Irrigation may be needed. Keep the soil reasonably moist.",
                "normal": "Moisture is suitable. Continue monitoring.",
                "wet": "Avoid excess irrigation and check drainage."
            },

            "Brinjal": {
                "dry": "Irrigation may be needed. Keep soil moisture reasonably consistent.",
                "normal": "Moisture is suitable. Continue monitoring.",
                "wet": "Avoid extra irrigation and check for waterlogging."
            },

            "Okra": {
                "dry": "Irrigation may be needed. Check the soil around the plants before watering.",
                "normal": "Moisture is reasonable. Continue monitoring.",
                "wet": "Avoid unnecessary irrigation and check drainage."
            },

            "Peas": {
                "dry": "Irrigation may be needed, but avoid overwatering.",
                "normal": "Moisture is suitable. Continue monitoring.",
                "wet": "Avoid irrigation because peas do not perform well in waterlogged soil."
            },

            "Cotton": {
                "dry": "Check the soil and irrigate if the crop needs water.",
                "normal": "Moisture is reasonable. Avoid unnecessary irrigation.",
                "wet": "Avoid extra irrigation and check for waterlogging."
            },

            "Bajra": {
                "dry": "Bajra can tolerate some dryness, but irrigate if the crop shows water stress.",
                "normal": "Moisture is suitable. Continue monitoring.",
                "wet": "Avoid excess irrigation and check drainage."
            },

            "Groundnut": {
                "dry": "Irrigation may be needed. Pay attention to moisture during pod development.",
                "normal": "Moisture is reasonable. Continue monitoring.",
                "wet": "Avoid excess water because waterlogging can damage the crop."
            },

            "Soybean": {
                "dry": "Irrigation may be needed if the soil is dry, especially during important growth stages.",
                "normal": "Moisture is reasonable. Continue monitoring.",
                "wet": "Avoid irrigation and check for waterlogging."
            }
        }

    else:

        crop_advice = {
            "Rice": {
                "dry": "चावल को नियमित पानी की जरूरत होती है। फसल की अवस्था के अनुसार सिंचाई करें।",
                "normal": "मिट्टी में अभी उचित नमी है। बिना जरूरत सिंचाई न करें।",
                "wet": "अभी अतिरिक्त पानी न दें। खेत में ज्यादा पानी जमा है तो निकासी करें।"
            },

            "Sugarcane": {
                "dry": "गन्ने को नियमित नमी चाहिए। मिट्टी सूखी है तो सिंचाई करें।",
                "normal": "मिट्टी में नमी उचित है। नियमित निगरानी करते रहें।",
                "wet": "अतिरिक्त सिंचाई न करें और पानी की निकासी जांचें।"
            },

            "Wheat": {
                "dry": "सिंचाई की जरूरत हो सकती है। पानी देने से पहले जड़ों के पास की मिट्टी जांचें।",
                "normal": "मिट्टी में नमी ठीक है। जरूरत होने पर ही सिंचाई करें।",
                "wet": "अभी सिंचाई न करें। ज्यादा पानी फसल को नुकसान पहुंचा सकता है।"
            },

            "Potato": {
                "dry": "आलू को लगातार नमी चाहिए। मिट्टी सूखी है तो सिंचाई करें।",
                "normal": "मिट्टी में नमी ठीक है। नियमित निगरानी करें।",
                "wet": "अतिरिक्त सिंचाई न करें। ज्यादा पानी जड़ों और कंद को नुकसान पहुंचा सकता है।"
            },

            "Maize": {
                "dry": "सिंचाई की जरूरत हो सकती है। फसल की महत्वपूर्ण विकास अवस्था में खास ध्यान दें।",
                "normal": "मिट्टी में नमी ठीक है। मिट्टी की नियमित जांच करते रहें।",
                "wet": "अतिरिक्त सिंचाई न करें और खेत में जलभराव की जांच करें।"
            },

            "Chana": {
                "dry": "मिट्टी सूखी है तो सिंचाई की जरूरत हो सकती है। ज्यादा पानी न दें।",
                "normal": "मिट्टी में नमी ठीक है। फसल की निगरानी करते रहें।",
                "wet": "अभी सिंचाई न करें। खेत में पानी जमा न होने दें।"
            },

            "Mustard": {
                "dry": "मिट्टी सूखी है तो सिंचाई की जरूरत हो सकती है, खासकर महत्वपूर्ण विकास अवस्था में।",
                "normal": "मिट्टी में नमी ठीक है। बिना जरूरत सिंचाई न करें।",
                "wet": "सिंचाई न करें और खेत में पानी की निकासी जांचें।"
            },

            "Tomato": {
                "dry": "टमाटर को नियमित नमी चाहिए। मिट्टी सूखी है तो सिंचाई करें।",
                "normal": "मिट्टी में नमी ठीक है। जरूरत के अनुसार पानी देते रहें।",
                "wet": "अतिरिक्त सिंचाई न करें क्योंकि ज्यादा पानी से रोग बढ़ सकते हैं।"
            },

            "Onion": {
                "dry": "सिंचाई की जरूरत हो सकती है। मिट्टी में नमी समान रखने की कोशिश करें।",
                "normal": "मिट्टी में नमी ठीक है। निगरानी करते रहें।",
                "wet": "अभी सिंचाई न करें और अतिरिक्त पानी निकलने दें।"
            },

            "Carrot": {
                "dry": "सिंचाई की जरूरत हो सकती है। अच्छी जड़ बनने के लिए मिट्टी में नमी रखें।",
                "normal": "मिट्टी में नमी ठीक है। नियमित निगरानी करें।",
                "wet": "अधिक पानी न दें क्योंकि जलभराव से जड़ों को नुकसान हो सकता है।"
            },

            "Bottle Gourd": {
                "dry": "लौकी को नियमित नमी चाहिए। मिट्टी सूखी है तो सिंचाई करें।",
                "normal": "मिट्टी में नमी ठीक है। निगरानी करते रहें।",
                "wet": "अतिरिक्त सिंचाई न करें और पानी की निकासी जांचें।"
            },

            "Cauliflower": {
                "dry": "सिंचाई की जरूरत हो सकती है। मिट्टी में नियमित नमी बनाए रखें।",
                "normal": "मिट्टी में नमी ठीक है। निगरानी करते रहें।",
                "wet": "अतिरिक्त सिंचाई न करें और जलभराव की जांच करें।"
            },

            "Cabbage": {
                "dry": "सिंचाई की जरूरत हो सकती है। मिट्टी में उचित नमी रखें।",
                "normal": "मिट्टी में नमी ठीक है। निगरानी करते रहें।",
                "wet": "अधिक सिंचाई न करें और पानी की निकासी जांचें।"
            },

            "Brinjal": {
                "dry": "सिंचाई की जरूरत हो सकती है। मिट्टी में नमी समान रखने की कोशिश करें।",
                "normal": "मिट्टी में नमी ठीक है। निगरानी करते रहें।",
                "wet": "अतिरिक्त सिंचाई न करें और जलभराव की जांच करें।"
            },

            "Okra": {
                "dry": "सिंचाई की जरूरत हो सकती है। पानी देने से पहले पौधों के पास की मिट्टी जांचें।",
                "normal": "मिट्टी में नमी ठीक है। निगरानी करते रहें।",
                "wet": "बिना जरूरत सिंचाई न करें और पानी की निकासी जांचें।"
            },

            "Peas": {
                "dry": "सिंचाई की जरूरत हो सकती है, लेकिन ज्यादा पानी न दें।",
                "normal": "मिट्टी में नमी ठीक है। निगरानी करते रहें।",
                "wet": "अभी सिंचाई न करें क्योंकि मटर को जलभराव पसंद नहीं है।"
            },

            "Cotton": {
                "dry": "मिट्टी की जांच करें और जरूरत होने पर सिंचाई करें।",
                "normal": "मिट्टी में नमी ठीक है। बिना जरूरत सिंचाई न करें।",
                "wet": "अतिरिक्त सिंचाई न करें और जलभराव की जांच करें।"
            },

            "Bajra": {
                "dry": "बाजरा कुछ सूखे को सहन कर सकता है, लेकिन फसल में पानी की कमी दिखे तो सिंचाई करें।",
                "normal": "मिट्टी में नमी ठीक है। निगरानी करते रहें।",
                "wet": "अधिक सिंचाई न करें और पानी की निकासी जांचें।"
            },

            "Groundnut": {
                "dry": "सिंचाई की जरूरत हो सकती है। फलियों के विकास के समय मिट्टी की नमी पर ध्यान दें।",
                "normal": "मिट्टी में नमी ठीक है। निगरानी करते रहें।",
                "wet": "अधिक पानी न दें क्योंकि जलभराव से फसल को नुकसान हो सकता है।"
            },

            "Soybean": {
                "dry": "मिट्टी सूखी है तो सिंचाई की जरूरत हो सकती है, खासकर महत्वपूर्ण विकास अवस्था में।",
                "normal": "मिट्टी में नमी ठीक है। निगरानी करते रहें।",
                "wet": "सिंचाई न करें और खेत में जलभराव की जांच करें।"
            }
        }

    
    st.subheader(advice_title)

    if soil_condition == dry_option:
        condition_key = "dry"

    elif soil_condition == normal_option:
        condition_key = "normal"

    else:
        condition_key = "wet"

    st.info(crop_advice[crop][condition_key])

    

    if soil_condition == dry_option:

        if language == "English":
            st.warning(
                "Before irrigation, check the soil near the crop roots. "
                "If it is dry, irrigation may be needed."
            )
        else:
            st.warning(
                "सिंचाई से पहले फसल की जड़ों के पास की मिट्टी जांचें। "
                "अगर मिट्टी सूखी है तो सिंचाई की जरूरत हो सकती है।"
            )

    elif soil_condition == normal_option:

        if language == "English":
            st.success(
                "No immediate irrigation may be needed. Keep checking the field."
            )
        else:
            st.success(
                "तुरंत सिंचाई की जरूरत नहीं हो सकती। खेत की निगरानी करते रहें।"
            )

    else:

        if language == "English":
            st.success(
                "Do not irrigate now. Allow excess water to drain from the field."
            )
        else:
            st.success(
                "अभी सिंचाई न करें। खेत से अतिरिक्त पानी निकलने दें।"
            )

    
    if language == "English":
        st.caption(
            "Note: Irrigation needs also depend on crop stage, soil type, rainfall and local conditions. "
            "This is general guidance."
        )
    else:
        st.caption(
            "नोट: सिंचाई की जरूरत फसल की अवस्था, मिट्टी, बारिश और स्थानीय परिस्थितियों पर भी निर्भर करती है। "
            "यह सामान्य सलाह है।"
        )

if option == "Irrigation":
    show_irrigation()


def show_fertilizer():
    
    if language == "English":
        heading = "Fertilizer Advisory"
        crop_label = "Select Crop"
        stage_label = "Which stage is the crop in?"
        sowing = "Sowing / Planting"
        vegetative = "Plant Growth"
        flowering = "Flowering / Fruit Development"

        general_note = (
            "Fertilizer needs depend on soil type, soil test, crop variety "
            "and local recommendations. Do not apply extra fertilizer without need."
        )

        nutrient_title = "Main Nutrient Need"
        why_title = "Why is it needed?"
        action_title = "What should you do?"

    else:
        heading = "उर्वरक की सलाह"
        crop_label = "फसल चुनें"
        stage_label = "फसल किस अवस्था में है?"
        sowing = "बुवाई / रोपाई"
        vegetative = "पौधे की बढ़वार"
        flowering = "फूल / फल बनने की अवस्था"

        general_note = (
            "उर्वरक की जरूरत मिट्टी, मिट्टी की जांच, फसल की किस्म "
            "और स्थानीय कृषि सलाह पर निर्भर करती है। बिना जरूरत अधिक उर्वरक न डालें।"
        )

        nutrient_title = "मुख्य पोषक तत्व की जरूरत"
        why_title = "इसकी जरूरत क्यों है?"
        action_title = "आपको क्या करना चाहिए?"

    st.subheader(heading)

    
    crop_names = {
        crop_data["Wheat"]["name"][language]: "Wheat",
        crop_data["Rice"]["name"][language]: "Rice",
        crop_data["Potato"]["name"][language]: "Potato",
        crop_data["Maize"]["name"][language]: "Maize",
        crop_data["Chana"]["name"][language]: "Chana",
        crop_data["Mustard"]["name"][language]: "Mustard",
        crop_data["Sugarcane"]["name"][language]: "Sugarcane",
        crop_data["Tomato"]["name"][language]: "Tomato",
        crop_data["Onion"]["name"][language]: "Onion",
        crop_data["Carrot"]["name"][language]: "Carrot",
        crop_data["Bottle Gourd"]["name"][language]: "Bottle Gourd",
        crop_data["Cauliflower"]["name"][language]: "Cauliflower",
        crop_data["Cabbage"]["name"][language]: "Cabbage",
        crop_data["Brinjal"]["name"][language]: "Brinjal",
        crop_data["Okra"]["name"][language]: "Okra",
        crop_data["Peas"]["name"][language]: "Peas",
        crop_data["Cotton"]["name"][language]: "Cotton",
        crop_data["Bajra"]["name"][language]: "Bajra",
        crop_data["Groundnut"]["name"][language]: "Groundnut",
        crop_data["Soybean"]["name"][language]: "Soybean"
    }

    selected_crop = st.selectbox(
        crop_label,
        list(crop_names.keys())
    )

    crop = crop_names[selected_crop]



    selected_stage = st.selectbox(
        stage_label,
        [
            sowing,
            vegetative,
            flowering
        ]
    )

    if selected_stage == sowing:
        stage = "Sowing"
    elif selected_stage == vegetative:
        stage = "Vegetative"
    else:
        stage = "Flowering"

    
    st.info(general_note)

   

    advice = {

        "Wheat": {
            "Sowing": {
                "nutrient": "Phosphorus + balanced nutrients",
                "why": "Supports early root development and healthy establishment.",
                "action": "Use the fertilizer recommended for your soil test. DAP or another phosphorus source may be recommended at sowing depending on soil condition."
            },
            "Vegetative": {
                "nutrient": "Nitrogen",
                "why": "Supports leaf and stem growth and helps maintain healthy crop growth.",
                "action": "Apply nitrogen in split doses according to local recommendation rather than applying the full amount at once."
            },
            "Flowering": {
                "nutrient": "Balanced nutrition",
                "why": "The crop needs proper nutrition while developing grains.",
                "action": "Do not add extra fertilizer blindly. Follow soil-test and local recommendations."
            }
        },

        "Rice": {
            "Sowing": {
                "nutrient": "Balanced NPK",
                "why": "Supports early root and plant development.",
                "action": "Use the recommended basal fertilizer according to soil-test results and local rice recommendations."
            },
            "Vegetative": {
                "nutrient": "Nitrogen",
                "why": "Helps leaf and plant growth.",
                "action": "Nitrogen is commonly applied in split doses. Follow the recommended schedule for your area."
            },
            "Flowering": {
                "nutrient": "Balanced nutrition",
                "why": "Supports healthy panicle and grain development.",
                "action": "Avoid unnecessary fertilizer. Follow local recommendations based on crop condition."
            }
        },

        "Potato": {
            "Sowing": {
                "nutrient": "Balanced NPK",
                "why": "Supports root development and early plant growth.",
                "action": "Apply the recommended basal fertilizer before or during planting according to soil-test guidance."
            },
            "Vegetative": {
                "nutrient": "Nitrogen + Potassium",
                "why": "Supports plant growth and healthy tuber development.",
                "action": "Use fertilizer according to crop stage and local recommendation. Avoid excessive nitrogen."
            },
            "Flowering": {
                "nutrient": "Potassium + balanced nutrition",
                "why": "Supports tuber development and crop quality.",
                "action": "Avoid excessive nitrogen and follow local fertilizer recommendations."
            }
        },

        "Maize": {
            "Sowing": {
                "nutrient": "Nitrogen + Phosphorus",
                "why": "Supports early roots and strong plant establishment.",
                "action": "Use the recommended basal fertilizer according to soil test."
            },
            "Vegetative": {
                "nutrient": "Nitrogen",
                "why": "Supports rapid leaf and stem growth.",
                "action": "Apply nitrogen in split doses according to local recommendation."
            },
            "Flowering": {
                "nutrient": "Balanced nutrition",
                "why": "Supports cob and grain development.",
                "action": "Do not apply extra fertilizer without checking crop condition and local advice."
            }
        },

        "Chana": {
            "Sowing": {
                "nutrient": "Phosphorus",
                "why": "Supports root development and early crop establishment.",
                "action": "Use phosphorus according to soil-test and local recommendations."
            },
            "Vegetative": {
                "nutrient": "Balanced nutrition",
                "why": "Supports healthy plant growth without excessive leafy growth.",
                "action": "Avoid unnecessary nitrogen application."
            },
            "Flowering": {
                "nutrient": "Balanced nutrition",
                "why": "Supports flowering and pod development.",
                "action": "Follow local recommendations and avoid excessive fertilizer."
            }
        },

        "Mustard": {
            "Sowing": {
                "nutrient": "Nitrogen + Phosphorus + Sulphur",
                "why": "Supports early growth and healthy oilseed development.",
                "action": "Sulphur can be important in mustard. Apply nutrients according to soil-test recommendations."
            },
            "Vegetative": {
                "nutrient": "Nitrogen + Sulphur",
                "why": "Supports plant growth and healthy leaf development.",
                "action": "Use the recommended nitrogen and sulphur schedule for your area."
            },
            "Flowering": {
                "nutrient": "Balanced nutrition",
                "why": "Supports flowering and pod formation.",
                "action": "Avoid unnecessary fertilizer at this stage and follow local recommendations."
            }
        },

        "Sugarcane": {
            "Sowing": {
                "nutrient": "Nitrogen + Phosphorus + Potassium",
                "why": "Supports strong roots and early cane establishment.",
                "action": "Apply basal nutrients according to soil test and local sugarcane recommendations."
            },
            "Vegetative": {
                "nutrient": "Nitrogen + Potassium",
                "why": "Supports active cane growth and healthy stems.",
                "action": "Nitrogen is generally applied in split doses. Follow the recommended schedule."
            },
            "Flowering": {
                "nutrient": "Balanced nutrition",
                "why": "Supports continued cane growth and quality.",
                "action": "Avoid excess nitrogen and follow local agricultural recommendations."
            }
        },

        "Tomato": {
            "Sowing": {
                "nutrient": "Balanced NPK",
                "why": "Supports strong roots and early plant growth.",
                "action": "Use compost or recommended basal fertilizer according to soil condition."
            },
            "Vegetative": {
                "nutrient": "Nitrogen + balanced nutrients",
                "why": "Supports healthy leaves and branches.",
                "action": "Do not use too much nitrogen because excessive leafy growth can reduce fruiting."
            },
            "Flowering": {
                "nutrient": "Potassium + balanced nutrition",
                "why": "Supports flowering and fruit development.",
                "action": "Maintain balanced nutrition and follow local fertilizer recommendations."
            }
        },

        "Onion": {
            "Sowing": {
                "nutrient": "Phosphorus + balanced NPK",
                "why": "Supports root establishment and early growth.",
                "action": "Apply recommended basal fertilizer according to soil test."
            },
            "Vegetative": {
                "nutrient": "Nitrogen",
                "why": "Supports healthy leaf growth and bulb development.",
                "action": "Use nitrogen according to the recommended schedule and avoid excessive application."
            },
            "Flowering": {
                "nutrient": "Potassium + balanced nutrition",
                "why": "Supports bulb development and crop quality.",
                "action": "Follow local recommendations and avoid excessive nitrogen."
            }
        },

        "Carrot": {
            "Sowing": {
                "nutrient": "Phosphorus + balanced nutrients",
                "why": "Supports root development.",
                "action": "Use well-balanced fertilizer based on soil testing."
            },
            "Vegetative": {
                "nutrient": "Balanced nutrition",
                "why": "Supports healthy leaf growth and root development.",
                "action": "Avoid excessive nitrogen because the main crop is the root."
            },
            "Flowering": {
                "nutrient": "Balanced nutrition",
                "why": "Carrot is harvested for its root rather than flowers.",
                "action": "Focus on proper soil moisture and balanced nutrition rather than adding unnecessary fertilizer."
            }
        },

        "Bottle Gourd": {
            "Sowing": {
                "nutrient": "Balanced NPK + organic matter",
                "why": "Supports strong roots and early vine growth.",
                "action": "Use well-decomposed organic manure and recommended fertilizer according to soil condition."
            },
            "Vegetative": {
                "nutrient": "Nitrogen + balanced nutrients",
                "why": "Supports healthy vine and leaf growth.",
                "action": "Avoid excessive nitrogen and maintain balanced nutrition."
            },
            "Flowering": {
                "nutrient": "Potassium + balanced nutrition",
                "why": "Supports flowering and fruit development.",
                "action": "Maintain balanced nutrition and follow local recommendations."
            }
        },

        "Cauliflower": {
            "Sowing": {
                "nutrient": "Balanced NPK + organic matter",
                "why": "Supports healthy root and early plant development.",
                "action": "Apply well-decomposed organic manure and recommended basal fertilizer."
            },
            "Vegetative": {
                "nutrient": "Nitrogen",
                "why": "Supports healthy leaf growth before curd development.",
                "action": "Apply nitrogen according to crop stage and local recommendation."
            },
            "Flowering": {
                "nutrient": "Potassium + balanced nutrition",
                "why": "Supports healthy curd development.",
                "action": "Maintain balanced nutrition and avoid excessive nitrogen."
            }
        },

        "Cabbage": {
            "Sowing": {
                "nutrient": "Balanced NPK + organic matter",
                "why": "Supports root establishment and early growth.",
                "action": "Use recommended basal fertilizer according to soil condition."
            },
            "Vegetative": {
                "nutrient": "Nitrogen",
                "why": "Supports leaf growth and head formation.",
                "action": "Apply nitrogen according to local recommendation and crop condition."
            },
            "Flowering": {
                "nutrient": "Potassium + balanced nutrition",
                "why": "Supports head development and crop quality.",
                "action": "Avoid excessive nitrogen and follow local recommendations."
            }
        },

        "Brinjal": {
            "Sowing": {
                "nutrient": "Balanced NPK + organic matter",
                "why": "Supports strong roots and early plant growth.",
                "action": "Use recommended basal fertilizer and well-decomposed organic manure."
            },
            "Vegetative": {
                "nutrient": "Nitrogen + balanced nutrients",
                "why": "Supports healthy leaves and branches.",
                "action": "Apply nutrients according to crop growth and avoid excessive nitrogen."
            },
            "Flowering": {
                "nutrient": "Potassium + balanced nutrition",
                "why": "Supports flowering and fruit development.",
                "action": "Maintain balanced nutrition and follow local recommendations."
            }
        },

        "Okra": {
            "Sowing": {
                "nutrient": "Balanced NPK",
                "why": "Supports early root and plant development.",
                "action": "Apply recommended basal fertilizer according to soil condition."
            },
            "Vegetative": {
                "nutrient": "Nitrogen",
                "why": "Supports healthy leaf and stem growth.",
                "action": "Use nitrogen according to local recommendation and avoid over-application."
            },
            "Flowering": {
                "nutrient": "Potassium + balanced nutrition",
                "why": "Supports flowering and pod development.",
                "action": "Maintain balanced nutrition and follow local recommendations."
            }
        },

        "Peas": {
            "Sowing": {
                "nutrient": "Phosphorus + balanced nutrients",
                "why": "Supports root development and early growth.",
                "action": "Use phosphorus according to soil-test recommendations."
            },
            "Vegetative": {
                "nutrient": "Balanced nutrition",
                "why": "Supports healthy plant growth.",
                "action": "Avoid excessive nitrogen because peas are a legume crop."
            },
            "Flowering": {
                "nutrient": "Potassium + balanced nutrition",
                "why": "Supports flowering and pod development.",
                "action": "Follow local recommendations and avoid unnecessary fertilizer."
            }
        },

        "Cotton": {
            "Sowing": {
                "nutrient": "Balanced NPK",
                "why": "Supports early root and plant establishment.",
                "action": "Apply recommended basal fertilizer according to soil test."
            },
            "Vegetative": {
                "nutrient": "Nitrogen + Potassium",
                "why": "Supports plant growth and healthy branches.",
                "action": "Apply nitrogen in suitable split doses and avoid excessive nitrogen."
            },
            "Flowering": {
                "nutrient": "Potassium + balanced nutrition",
                "why": "Supports boll development and crop strength.",
                "action": "Follow local fertilizer recommendations and avoid excess nitrogen."
            }
        },

        "Bajra": {
            "Sowing": {
                "nutrient": "Nitrogen + Phosphorus",
                "why": "Supports early root and plant establishment.",
                "action": "Use recommended basal fertilizer according to soil condition."
            },
            "Vegetative": {
                "nutrient": "Nitrogen",
                "why": "Supports leaf and plant growth.",
                "action": "Apply nitrogen according to local recommendation."
            },
            "Flowering": {
                "nutrient": "Balanced nutrition",
                "why": "Supports ear and grain development.",
                "action": "Avoid unnecessary fertilizer and follow local recommendations."
            }
        },

        "Groundnut": {
            "Sowing": {
                "nutrient": "Phosphorus + Calcium + Sulphur",
                "why": "Supports roots, flowering and pod development.",
                "action": "Apply nutrients according to soil-test results. Calcium and sulphur may be important depending on soil condition."
            },
            "Vegetative": {
                "nutrient": "Balanced nutrition",
                "why": "Supports healthy plant growth.",
                "action": "Avoid excessive nitrogen and follow local recommendations."
            },
            "Flowering": {
                "nutrient": "Calcium + Sulphur + balanced nutrition",
                "why": "Supports pod formation and healthy seed development.",
                "action": "Follow local recommendations based on soil and crop condition."
            }
        },

        "Soybean": {
            "Sowing": {
                "nutrient": "Phosphorus + Potassium",
                "why": "Supports early root development and crop establishment.",
                "action": "Use fertilizer according to soil-test and local recommendations."
            },
            "Vegetative": {
                "nutrient": "Balanced nutrition",
                "why": "Supports healthy plant growth.",
                "action": "Avoid unnecessary nitrogen because soybean is a legume."
            },
            "Flowering": {
                "nutrient": "Potassium + balanced nutrition",
                "why": "Supports flowering and pod development.",
                "action": "Follow local fertilizer recommendations and avoid excessive application."
            }
        }
    }

    selected_advice = advice[crop][stage]

    if language == "हिंदी":

        hindi_nutrients = {
            "Phosphorus": "फास्फोरस",
            "Nitrogen": "नाइट्रोजन",
            "Potassium": "पोटाश",
            "Sulphur": "सल्फर",
            "Calcium": "कैल्शियम",
            "Balanced NPK": "संतुलित NPK",
            "Balanced nutrition": "संतुलित पोषण",
            "Phosphorus + balanced nutrients": "फास्फोरस + संतुलित पोषक तत्व",
            "Phosphorus + balanced NPK": "फास्फोरस + संतुलित NPK",
            "Nitrogen + Phosphorus": "नाइट्रोजन + फास्फोरस",
            "Nitrogen + Potassium": "नाइट्रोजन + पोटाश",
            "Nitrogen + Phosphorus + Sulphur": "नाइट्रोजन + फास्फोरस + सल्फर",
            "Nitrogen + Potassium": "नाइट्रोजन + पोटाश",
            "Potassium + balanced nutrition": "पोटाश + संतुलित पोषण",
            "Balanced NPK + organic matter": "संतुलित NPK + जैविक पदार्थ",
            "Nitrogen + balanced nutrients": "नाइट्रोजन + संतुलित पोषक तत्व",
            "Phosphorus + Calcium + Sulphur": "फास्फोरस + कैल्शियम + सल्फर",
            "Calcium + Sulphur + balanced nutrition": "कैल्शियम + सल्फर + संतुलित पोषण",
            "Phosphorus + Potassium": "फास्फोरस + पोटाश"
        }

        nutrient = selected_advice["nutrient"]
        nutrient_hi = hindi_nutrients.get(nutrient, nutrient)

        why_templates = {
            "Sowing": "यह पोषक तत्व शुरुआती जड़ विकास और फसल की अच्छी शुरुआत में मदद करता है।",
            "Vegetative": "यह पोषक तत्व पौधे की स्वस्थ बढ़वार में मदद करता है।",
            "Flowering": "यह पोषक तत्व फूल, फल या दाने के अच्छे विकास में मदद करता है।"
        }

        action_templates = {
            "Sowing": "मिट्टी की जांच और स्थानीय कृषि सलाह के अनुसार बुवाई के समय अनुशंसित उर्वरक का उपयोग करें।",
            "Vegetative": "फसल की अवस्था और स्थानीय कृषि सलाह के अनुसार उर्वरक दें। एक बार में जरूरत से ज्यादा उर्वरक न डालें।",
            "Flowering": "स्थानीय कृषि सलाह के अनुसार संतुलित पोषण दें और बिना जरूरत अतिरिक्त उर्वरक न डालें।"
        }

        st.subheader(nutrient_title)
        st.info(nutrient_hi)

        st.subheader(why_title)
        st.write(why_templates[stage])

        st.subheader(action_title)
        st.write(action_templates[stage])

    else:

        st.subheader(nutrient_title)
        st.info(selected_advice["nutrient"])

        st.subheader(why_title)
        st.write(selected_advice["why"])

        st.subheader(action_title)
        st.write(selected_advice["action"])

    

    if language == "English":
        st.warning(
            "Do not increase fertilizer quantity just to increase yield. "
            "Excess fertilizer can waste money and may damage soil or crops."
        )
    else:
        st.warning(
            "सिर्फ उपज बढ़ाने के लिए उर्वरक की मात्रा न बढ़ाएं। "
            "अधिक उर्वरक से पैसा बर्बाद हो सकता है और मिट्टी या फसल को नुकसान हो सकता है।"
        )

    
    if language == "English":
        st.caption(
            "For exact fertilizer type and quantity, use a soil test and follow "
            "recommendations from your local agriculture department or qualified expert."
        )
    else:
        st.caption(
            "उर्वरक के सही प्रकार और मात्रा के लिए मिट्टी की जांच कराएं और "
            "स्थानीय कृषि विभाग या योग्य कृषि विशेषज्ञ की सलाह लें।"
        )

if option == "Fertilizer":
    show_fertilizer()
        
        

def show_weather():
    
    if language == "English":
        city_label = "Enter your city"
        city_help = "Enter a city name to get its current weather."
        search_button = "Get Weather"
        weather_title = "Current Weather"
        humidity_text = "Humidity"
        feels_like_text = "Feels Like"
        wind_text = "Wind Speed"
        condition_text = "Condition"
        location_text = "Weather for"
        error_city = "City not found. Please check the city name."
        error_weather = "Unable to get weather data. Please try again."
    else:
        city_label = "अपने शहर का नाम लिखें"
        city_help = "अपने शहर का वर्तमान मौसम देखने के लिए शहर का नाम लिखें।"
        search_button = "मौसम देखें"
        weather_title = "वर्तमान मौसम"
        humidity_text = "नमी"
        feels_like_text = "महसूस होने वाला तापमान"
        wind_text = "हवा की गति"
        condition_text = "मौसम की स्थिति"
        location_text = "मौसम"
        error_city = "शहर नहीं मिला। कृपया शहर का नाम जांचें।"
        error_weather = "मौसम की जानकारी प्राप्त नहीं हो सकी। कृपया दोबारा प्रयास करें।"

    city = st.text_input(city_label, placeholder="e.g. Lucknow", help=city_help)

    if st.button(search_button, use_container_width=True):

        if not city.strip():
            st.warning(city_label)
            return

        try:
            geo_url = "https://geocoding-api.open-meteo.com/v1/search"

            geo_params = {
                "name": city,
                "count": 1,
                "language": "en",
                "format": "json"
            }

            geo_response = requests.get(
                geo_url,
                params=geo_params,
                timeout=10
            )

            geo_data = geo_response.json()

            if "results" not in geo_data:
                st.error(error_city)
                return

            location = geo_data["results"][0]

            latitude = location["latitude"]
            longitude = location["longitude"]
            location_name = location["name"]
            country = location.get("country", "")

            weather_url = "https://api.open-meteo.com/v1/forecast"

            weather_params = {
                "latitude": latitude,
                "longitude": longitude,
                "current": "temperature_2m,relative_humidity_2m,apparent_temperature,weather_code,wind_speed_10m",
                "timezone": "auto"
            }

            weather_response = requests.get(
                weather_url,
                params=weather_params,
                timeout=10
            )

            weather_data = weather_response.json()
            current = weather_data["current"]

            weather_codes = {
                0: ("Clear sky", "साफ आसमान"),
                1: ("Mainly clear", "मुख्य रूप से साफ"),
                2: ("Partly cloudy", "आंशिक बादल"),
                3: ("Overcast", "बादल छाए हुए"),
                45: ("Fog", "कोहरा"),
                48: ("Depositing rime fog", "कोहरा"),
                51: ("Light drizzle", "हल्की बूंदाबांदी"),
                53: ("Moderate drizzle", "मध्यम बूंदाबांदी"),
                55: ("Dense drizzle", "तेज बूंदाबांदी"),
                61: ("Light rain", "हल्की बारिश"),
                63: ("Moderate rain", "मध्यम बारिश"),
                65: ("Heavy rain", "तेज बारिश"),
                71: ("Light snow", "हल्की बर्फबारी"),
                73: ("Moderate snow", "मध्यम बर्फबारी"),
                75: ("Heavy snow", "तेज बर्फबारी"),
                80: ("Light rain showers", "हल्की बारिश"),
                81: ("Moderate rain showers", "मध्यम बारिश"),
                82: ("Heavy rain showers", "तेज बारिश"),
                95: ("Thunderstorm", "आंधी-तूफान"),
                96: ("Thunderstorm with hail", "ओलावृष्टि के साथ आंधी"),
                99: ("Thunderstorm with heavy hail", "तेज ओलावृष्टि के साथ आंधी")
            }

            code = current["weather_code"]

            if language == "English":
                condition = weather_codes.get(code, ("Unknown", "अज्ञात"))[0]
            else:
                condition = weather_codes.get(code, ("Unknown", "अज्ञात"))[1]

            st.subheader(weather_title)
            st.write(f"{location_text}: {location_name}, {country}")

            col1, col2, col3 = st.columns(3)

            with col1:
                st.metric(
                    "Temperature" if language == "English" else "तापमान",
                    f"{current['temperature_2m']} °C"
                )

            with col2:
                st.metric(
                    humidity_text,
                    f"{current['relative_humidity_2m']}%"
                )

            with col3:
                st.metric(
                    feels_like_text,
                    f"{current['apparent_temperature']} °C"
                )

            col4, col5 = st.columns(2)

            with col4:
                st.metric(
                    wind_text,
                    f"{current['wind_speed_10m']} km/h"
                )

            with col5:
                st.metric(
                    condition_text,
                    condition
                )

            st.caption(
                "Weather data is updated automatically from Open-Meteo."
                if language == "English"
                else
                "मौसम की जानकारी Open-Meteo से अपने आप प्राप्त होती है।"
            )

        except Exception:
            st.error(error_weather)
    
if option == "Weather":
    show_weather()
  
        
def show_crop_calendar():

    if language == "English":
        heading = "Crop Calendar"
        crop_label = "Select Crop"
        month_label = "Select Month"
        sowing_label = "Sowing / Planting"
        growth_label = "Growth Period"
        harvest_label = "Harvest"
        action_label = "What should you do?"
        note = "These dates are general guidance. Actual timing can change with region, weather and crop variety."
        months = [
            "January", "February", "March", "April",
            "May", "June", "July", "August",
            "September", "October", "November", "December"
        ]
    else:
        heading = "फसल कैलेंडर"
        crop_label = "फसल चुनें"
        month_label = "महीना चुनें"
        sowing_label = "बुवाई / रोपाई"
        growth_label = "विकास का समय"
        harvest_label = "कटाई"
        action_label = "आपको क्या करना चाहिए?"
        note = "ये तिथियां सामान्य जानकारी के लिए हैं। वास्तविक समय क्षेत्र, मौसम और फसल की किस्म के अनुसार बदल सकता है।"
        months = [
            "जनवरी", "फरवरी", "मार्च", "अप्रैल",
            "मई", "जून", "जुलाई", "अगस्त",
            "सितंबर", "अक्टूबर", "नवंबर", "दिसंबर"
        ]

    st.subheader(heading)

    crop_names = {
        crop_data["Wheat"]["name"][language]: "Wheat",
        crop_data["Rice"]["name"][language]: "Rice",
        crop_data["Potato"]["name"][language]: "Potato",
        crop_data["Maize"]["name"][language]: "Maize",
        crop_data["Chana"]["name"][language]: "Chana",
        crop_data["Mustard"]["name"][language]: "Mustard",
        crop_data["Sugarcane"]["name"][language]: "Sugarcane",
        crop_data["Tomato"]["name"][language]: "Tomato",
        crop_data["Onion"]["name"][language]: "Onion",
        crop_data["Carrot"]["name"][language]: "Carrot",
        crop_data["Bottle Gourd"]["name"][language]: "Bottle Gourd",
        crop_data["Cauliflower"]["name"][language]: "Cauliflower",
        crop_data["Cabbage"]["name"][language]: "Cabbage",
        crop_data["Brinjal"]["name"][language]: "Brinjal",
        crop_data["Okra"]["name"][language]: "Okra",
        crop_data["Peas"]["name"][language]: "Peas",
        crop_data["Cotton"]["name"][language]: "Cotton",
        crop_data["Bajra"]["name"][language]: "Bajra",
        crop_data["Groundnut"]["name"][language]: "Groundnut",
        crop_data["Soybean"]["name"][language]: "Soybean"
    }

    selected_crop = st.selectbox(
        crop_label,
        list(crop_names.keys())
    )

    selected_month = st.selectbox(
        month_label,
        months
    )

    crop = crop_names[selected_crop]

    calendar = {
        "Wheat": {
            "sowing": "October - December",
            "growth": "December - February",
            "harvest": "March - April",
            "months": ["October", "November", "December"],
            "actions": {
                "English": {
                    "January": "Crop growth stage. Monitor irrigation and weeds.",
                    "February": "Grain filling stage. Maintain proper irrigation and monitor the crop.",
                    "March": "Harvest period may begin. Check grain maturity before harvesting.",
                    "April": "Harvest period. Harvest when the crop is mature and dry.",
                    "May": "Prepare the field for the next suitable crop.",
                    "June": "Not the normal sowing period. Plan the next crop according to local conditions.",
                    "July": "Not the normal sowing period for wheat.",
                    "August": "Start planning seed and field preparation for the coming season.",
                    "September": "Prepare the field and arrange quality seed for sowing.",
                    "October": "Sowing period begins. Prepare soil and sow at the recommended time.",
                    "November": "Sowing period. Complete sowing in the suitable window.",
                    "December": "Early growth stage. Monitor weeds, moisture and plant growth."
                },
                "हिंदी": {
                    "जनवरी": "फसल की बढ़वार का समय है। सिंचाई और खरपतवार पर ध्यान दें।",
                    "फरवरी": "दाने भरने की अवस्था हो सकती है। उचित सिंचाई रखें और फसल की निगरानी करें।",
                    "मार्च": "कटाई शुरू हो सकती है। कटाई से पहले दानों की परिपक्वता जांचें।",
                    "अप्रैल": "कटाई का समय है। फसल पूरी तरह तैयार और सूखी होने पर कटाई करें।",
                    "मई": "अगली उपयुक्त फसल के लिए खेत तैयार करें।",
                    "जून": "गेहूं की सामान्य बुवाई का समय नहीं है। अगली फसल की योजना बनाएं।",
                    "जुलाई": "गेहूं की सामान्य बुवाई का समय नहीं है।",
                    "अगस्त": "आने वाले मौसम के लिए बीज और खेत की तैयारी की योजना बनाएं।",
                    "सितंबर": "खेत तैयार करें और अच्छी गुणवत्ता का बीज रखें।",
                    "अक्टूबर": "बुवाई का समय शुरू होता है। खेत तैयार करके उचित समय पर बुवाई करें।",
                    "नवंबर": "बुवाई का समय है। उचित समय में बुवाई पूरी करें।",
                    "दिसंबर": "शुरुआती बढ़वार का समय है। खरपतवार, नमी और पौधों की बढ़वार पर ध्यान दें।"
                }
            }
        },

        "Rice": {
            "sowing": "June - July",
            "growth": "July - September",
            "harvest": "October - November",
            "months": ["June", "July"],
            "actions": {
                "English": {
                    "January": "Plan the next crop and prepare the field if needed.",
                    "February": "Prepare seed and field plans for the coming season.",
                    "March": "Arrange quality seed and plan nursery or direct sowing.",
                    "April": "Prepare irrigation and field arrangements.",
                    "May": "Prepare nursery or field according to the local rice system.",
                    "June": "Main sowing or transplanting period begins in many areas.",
                    "July": "Sowing or transplanting period. Maintain moisture and control weeds.",
                    "August": "Active growth stage. Monitor water, weeds and pests.",
                    "September": "Grain development stage. Monitor crop health and water management.",
                    "October": "Harvest may begin for early varieties. Check grain maturity.",
                    "November": "Harvest period for many varieties. Dry harvested grain properly.",
                    "December": "Complete post-harvest work and prepare for the next crop."
                },
                "हिंदी": {
                    "जनवरी": "अगली फसल की योजना बनाएं और जरूरत हो तो खेत तैयार करें।",
                    "फरवरी": "आने वाले मौसम के लिए बीज और खेत की योजना बनाएं।",
                    "मार्च": "अच्छा बीज रखें और नर्सरी या सीधी बुवाई की योजना बनाएं।",
                    "अप्रैल": "सिंचाई और खेत की व्यवस्था तैयार करें।",
                    "मई": "स्थानीय पद्धति के अनुसार नर्सरी या खेत तैयार करें।",
                    "जून": "कई क्षेत्रों में बुवाई या रोपाई का मुख्य समय शुरू होता है।",
                    "जुलाई": "बुवाई या रोपाई का समय है। नमी रखें और खरपतवार नियंत्रित करें।",
                    "अगस्त": "फसल की सक्रिय बढ़वार है। पानी, खरपतवार और कीटों पर ध्यान दें।",
                    "सितंबर": "दाने बनने की अवस्था है। फसल और पानी की व्यवस्था पर ध्यान दें।",
                    "अक्टूबर": "जल्दी तैयार होने वाली किस्मों की कटाई शुरू हो सकती है। दाने की परिपक्वता जांचें।",
                    "नवंबर": "कई किस्मों में कटाई का समय है। कटाई के बाद अनाज को अच्छी तरह सुखाएं।",
                    "दिसंबर": "कटाई के बाद का काम पूरा करें और अगली फसल की तैयारी करें।"
                }
            }
        },

        "Potato": {
            "sowing": "October - November",
            "growth": "November - January",
            "harvest": "January - February",
            "months": ["October", "November"],
            "actions": {
                "English": {
                    "January": "Tubers are developing or nearing harvest. Monitor maturity and avoid unnecessary irrigation.",
                    "February": "Harvest period. Harvest mature tubers carefully and store them properly.",
                    "March": "Complete storage and prepare for the next suitable crop.",
                    "April": "Prepare field according to the next crop.",
                    "May": "Field preparation and planning period.",
                    "June": "Not the normal potato planting period in most areas.",
                    "July": "Not the normal planting period.",
                    "August": "Arrange quality seed potatoes for the coming season.",
                    "September": "Prepare soil and arrange healthy seed tubers.",
                    "October": "Planting period begins in suitable areas.",
                    "November": "Planting period. Complete planting in the suitable window.",
                    "December": "Early growth stage. Monitor moisture, weeds and plant health."
                },
                "हिंदी": {
                    "जनवरी": "कंद बन रहे हैं या कटाई के करीब हैं। परिपक्वता देखें और अनावश्यक सिंचाई न करें।",
                    "फरवरी": "कटाई का समय है। तैयार कंदों की सावधानी से खुदाई करें और सही तरीके से भंडारण करें।",
                    "मार्च": "भंडारण का काम पूरा करें और अगली उपयुक्त फसल की तैयारी करें।",
                    "अप्रैल": "अगली फसल के अनुसार खेत तैयार करें।",
                    "मई": "खेत की तैयारी और योजना बनाने का समय है।",
                    "जून": "अधिकांश क्षेत्रों में आलू की सामान्य बुवाई का समय नहीं है।",
                    "जुलाई": "सामान्य बुवाई का समय नहीं है।",
                    "अगस्त": "आने वाले मौसम के लिए अच्छे बीज आलू की व्यवस्था करें।",
                    "सितंबर": "मिट्टी तैयार करें और स्वस्थ बीज कंद रखें।",
                    "अक्टूबर": "उपयुक्त क्षेत्रों में रोपण का समय शुरू होता है।",
                    "नवंबर": "रोपण का समय है। उचित समय में रोपण पूरा करें।",
                    "दिसंबर": "शुरुआती बढ़वार है। नमी, खरपतवार और पौधों की स्थिति देखें।"
                }
            }
        },

        "Maize": {
            "sowing": "June - July",
            "growth": "July - September",
            "harvest": "September - October",
            "months": ["June", "July"],
            "actions": {
                "English": {
                    "January": "Plan the next suitable maize season.",
                    "February": "Arrange seed and prepare the field plan.",
                    "March": "Check seed quality and field requirements.",
                    "April": "Prepare irrigation and field arrangements.",
                    "May": "Prepare the field and arrange quality seed.",
                    "June": "Sowing period begins. Sow in suitable soil moisture.",
                    "July": "Sowing and early growth period. Control weeds and monitor moisture.",
                    "August": "Active growth stage. Monitor nutrients, moisture and pests.",
                    "September": "Grain development and early harvest period for some varieties.",
                    "October": "Harvest period for many crops. Check grain maturity before harvest.",
                    "November": "Complete post-harvest work and store grain properly.",
                    "December": "Prepare for the next crop."
                },
                "हिंदी": {
                    "जनवरी": "अगली उपयुक्त मक्का फसल की योजना बनाएं।",
                    "फरवरी": "बीज की व्यवस्था करें और खेत की योजना बनाएं।",
                    "मार्च": "बीज की गुणवत्ता और खेत की जरूरत जांचें।",
                    "अप्रैल": "सिंचाई और खेत की व्यवस्था तैयार करें।",
                    "मई": "खेत तैयार करें और अच्छा बीज रखें।",
                    "जून": "बुवाई का समय शुरू होता है। उचित नमी में बुवाई करें।",
                    "जुलाई": "बुवाई और शुरुआती बढ़वार का समय है। खरपतवार और नमी पर ध्यान दें।",
                    "अगस्त": "सक्रिय बढ़वार है। पोषक तत्व, नमी और कीटों पर ध्यान दें।",
                    "सितंबर": "दाने बनने और कुछ किस्मों में शुरुआती कटाई का समय है।",
                    "अक्टूबर": "कई फसलों में कटाई का समय है। कटाई से पहले दाने की परिपक्वता जांचें।",
                    "नवंबर": "कटाई के बाद का काम पूरा करें और अनाज को सही तरीके से रखें।",
                    "दिसंबर": "अगली फसल की तैयारी करें।"
                }
            }
        },

        "Chana": {
            "sowing": "October - November",
            "growth": "November - February",
            "harvest": "February - March",
            "months": ["October", "November"],
            "actions": {
                "English": {
                    "January": "Crop growth and pod development. Monitor moisture and pests.",
                    "February": "Harvest may begin. Check pod and plant maturity.",
                    "March": "Harvest period. Dry harvested crop properly before storage.",
                    "April": "Complete storage and field preparation.",
                    "May": "Plan the next crop.",
                    "June": "Not the normal sowing period.",
                    "July": "Not the normal sowing period.",
                    "August": "Arrange quality seed for the coming season.",
                    "September": "Prepare field and seed.",
                    "October": "Sowing period begins. Prepare soil and sow at the suitable time.",
                    "November": "Sowing period. Complete sowing in the suitable window.",
                    "December": "Early growth stage. Monitor weeds and crop health."
                },
                "हिंदी": {
                    "जनवरी": "फसल की बढ़वार और फलियों के विकास का समय है। नमी और कीटों पर ध्यान दें।",
                    "फरवरी": "कटाई शुरू हो सकती है। फलियों और पौधों की परिपक्वता जांचें।",
                    "मार्च": "कटाई का समय है। भंडारण से पहले फसल को अच्छी तरह सुखाएं।",
                    "अप्रैल": "भंडारण और खेत की तैयारी पूरी करें।",
                    "मई": "अगली फसल की योजना बनाएं।",
                    "जून": "सामान्य बुवाई का समय नहीं है।",
                    "जुलाई": "सामान्य बुवाई का समय नहीं है।",
                    "अगस्त": "आने वाले मौसम के लिए अच्छा बीज रखें।",
                    "सितंबर": "खेत और बीज तैयार करें।",
                    "अक्टूबर": "बुवाई का समय शुरू होता है। खेत तैयार करके उचित समय पर बुवाई करें।",
                    "नवंबर": "बुवाई का समय है। उचित समय में बुवाई पूरी करें।",
                    "दिसंबर": "शुरुआती बढ़वार है। खरपतवार और फसल की स्थिति देखें।"
                }
            }
        },

        "Mustard": {
            "sowing": "October - November",
            "growth": "November - February",
            "harvest": "February - March",
            "months": ["October", "November"],
            "actions": {
                "English": {
                    "January": "Flowering and pod development may occur. Monitor crop health.",
                    "February": "Harvest may begin. Watch for mature pods.",
                    "March": "Harvest period. Harvest when pods are mature and avoid unnecessary delay.",
                    "April": "Complete post-harvest work.",
                    "May": "Prepare for the next crop.",
                    "June": "Not the normal sowing period.",
                    "July": "Not the normal sowing period.",
                    "August": "Plan seed and field preparation.",
                    "September": "Prepare soil and quality seed.",
                    "October": "Sowing period begins.",
                    "November": "Complete sowing in the suitable period.",
                    "December": "Early crop growth. Monitor weeds and plant health."
                },
                "हिंदी": {
                    "जनवरी": "फूल और फलियों के विकास का समय हो सकता है। फसल की स्थिति देखें।",
                    "फरवरी": "कटाई शुरू हो सकती है। पकी हुई फलियों पर ध्यान दें।",
                    "मार्च": "कटाई का समय है। फलियां तैयार होने पर कटाई करें।",
                    "अप्रैल": "कटाई के बाद का काम पूरा करें।",
                    "मई": "अगली फसल की तैयारी करें।",
                    "जून": "सामान्य बुवाई का समय नहीं है।",
                    "जुलाई": "सामान्य बुवाई का समय नहीं है।",
                    "अगस्त": "बीज और खेत की तैयारी की योजना बनाएं।",
                    "सितंबर": "मिट्टी और अच्छा बीज तैयार करें।",
                    "अक्टूबर": "बुवाई का समय शुरू होता है।",
                    "नवंबर": "उचित समय में बुवाई पूरी करें।",
                    "दिसंबर": "शुरुआती बढ़वार है। खरपतवार और फसल की स्थिति देखें।"
                }
            }
        }
    }

    simple_calendar = {
        "Sugarcane": ("February - March", "March - December", "10 - 18 months"),
        "Tomato": ("September - November", "November - January", "60 - 90 days"),
        "Onion": ("October - December", "December - March", "March - April"),
        "Carrot": ("October - November", "November - January", "January - February"),
        "Bottle Gourd": ("February - March", "March - June", "May - July"),
        "Cauliflower": ("September - November", "November - January", "December - February"),
        "Cabbage": ("September - November", "November - January", "December - February"),
        "Brinjal": ("Suitable seasons", "2 - 3 months", "3 - 5 months"),
        "Okra": ("February - March / June - July", "March - August", "April - September"),
        "Peas": ("October - November", "November - January", "January - February"),
        "Cotton": ("April - June", "June - September", "October - January"),
        "Bajra": ("June - July", "July - September", "September - October"),
        "Groundnut": ("June - July", "July - September", "September - October"),
        "Soybean": ("June - July", "July - September", "September - October")
    }

    if crop in calendar:
        sowing_time = calendar[crop]["sowing"]
        growth_time = calendar[crop]["growth"]
        harvest_time = calendar[crop]["harvest"]
        action = calendar[crop]["actions"][language][selected_month]
    else:
        sowing_time, growth_time, harvest_time = simple_calendar[crop]

        if language == "English":
            action = {
                "January": "Check the crop stage and plan field activities according to local weather.",
                "February": "Prepare the field or monitor the existing crop according to its stage.",
                "March": "Check crop growth and prepare for the next field activity.",
                "April": "Prepare the field if the crop season is approaching.",
                "May": "Monitor weather and prepare for the coming crop season.",
                "June": "Rainy-season crops may begin sowing in suitable areas.",
                "July": "Monitor crop growth, weeds, moisture and pests.",
                "August": "Continue crop monitoring and maintain proper field conditions.",
                "September": "Monitor maturity and prepare for harvesting where applicable.",
                "October": "Harvest suitable crops or prepare fields for winter crops.",
                "November": "Many winter crops are planted during this period.",
                "December": "Monitor winter crops and maintain proper moisture and weed control."
            }[selected_month]
        else:
            action = {
                "जनवरी": "फसल की अवस्था देखें और स्थानीय मौसम के अनुसार खेत का काम करें।",
                "फरवरी": "फसल की अवस्था के अनुसार खेत तैयार करें या मौजूदा फसल की निगरानी करें।",
                "मार्च": "फसल की बढ़वार देखें और अगले कृषि कार्य की तैयारी करें।",
                "अप्रैल": "यदि फसल का मौसम पास है तो खेत की तैयारी करें।",
                "मई": "मौसम पर ध्यान दें और आने वाली फसल की तैयारी करें।",
                "जून": "उपयुक्त क्षेत्रों में खरीफ फसलों की बुवाई शुरू हो सकती है।",
                "जुलाई": "फसल की बढ़वार, खरपतवार, नमी और कीटों पर ध्यान दें।",
                "अगस्त": "फसल की निगरानी जारी रखें और खेत की स्थिति सही रखें।",
                "सितंबर": "जहां कटाई का समय हो वहां परिपक्वता देखें और कटाई की तैयारी करें।",
                "अक्टूबर": "उपयुक्त फसलों की कटाई करें या रबी फसलों के लिए खेत तैयार करें।",
                "नवंबर": "कई रबी फसलों की बुवाई इस समय होती है।",
                "दिसंबर": "रबी फसलों की नमी और खरपतवार पर ध्यान दें।"
            }[selected_month]

    st.info(note)

    st.subheader(sowing_label)
    st.write(sowing_time)

    st.subheader(growth_label)
    st.write(growth_time)

    st.subheader(harvest_label)
    st.write(harvest_time)

    st.subheader(action_label)
    st.success(action)

    if language == "English":
        st.caption("Use local agriculture recommendations when deciding exact sowing and harvesting dates.")
    else:
        st.caption("बुवाई और कटाई की सही तारीख तय करने के लिए स्थानीय कृषि सलाह का उपयोग करें।")

if option == "Crop Calendar":
    show_crop_calendar()
    

def show_pest_detection():
    
    st.subheader(text[language]["pest"])

    st.write(text[language]["pest_intro"])

    crop_names = {
        crop_data["Wheat"]["name"][language]: "Wheat",
        crop_data["Rice"]["name"][language]: "Rice",
        crop_data["Potato"]["name"][language]: "Potato",
        crop_data["Maize"]["name"][language]: "Maize",
        crop_data["Chana"]["name"][language]: "Chana",
        crop_data["Mustard"]["name"][language]: "Mustard",
        crop_data["Sugarcane"]["name"][language]: "Sugarcane",
        crop_data["Tomato"]["name"][language]: "Tomato",
        crop_data["Onion"]["name"][language]: "Onion",
        crop_data["Carrot"]["name"][language]: "Carrot",
        crop_data["Bottle Gourd"]["name"][language]: "Bottle Gourd",
        crop_data["Cauliflower"]["name"][language]: "Cauliflower",
        crop_data["Cabbage"]["name"][language]: "Cabbage",
        crop_data["Brinjal"]["name"][language]: "Brinjal",
        crop_data["Okra"]["name"][language]: "Okra",
        crop_data["Peas"]["name"][language]: "Peas",
        crop_data["Cotton"]["name"][language]: "Cotton",
        crop_data["Bajra"]["name"][language]: "Bajra",
        crop_data["Groundnut"]["name"][language]: "Groundnut",
        crop_data["Soybean"]["name"][language]: "Soybean"
    }

    selected_crop = st.selectbox(
        text[language]["select_crop_pest"],
        list(crop_names.keys())
    )

    crop = crop_names[selected_crop]

    pest_data = {

        "Wheat": {
            "problem": {
                "English": "Aphids, termites and rust diseases",
                "हिंदी": "माहू, दीमक और रतुआ रोग"
            },
            "symptoms": {
                "English": "Yellowing leaves, small insects on leaves and brown or orange rust spots.",
                "हिंदी": "पत्तियों का पीला होना, पत्तियों पर छोटे कीट और भूरे या नारंगी रतुआ के धब्बे।"
            }
        },

        "Rice": {
            "problem": {
                "English": "Stem borer, brown planthopper and blast disease",
                "हिंदी": "तना छेदक, भूरा माहू और झुलसा रोग"
            },
            "symptoms": {
                "English": "Dead central shoots, insects near the plant base and spots on leaves.",
                "हिंदी": "बीच की नई टहनियों का सूखना, पौधे के नीचे की तरफ कीट और पत्तियों पर धब्बे।"
            }
        },

        "Potato": {
            "problem": {
                "English": "Tuber moth, aphids and late blight",
                "हिंदी": "कंद पतंगा, माहू और पछेती झुलसा रोग"
            },
            "symptoms": {
                "English": "Damaged leaves, small insects and dark spots spreading on leaves.",
                "हिंदी": "पत्तियों का खराब होना, छोटे कीट और पत्तियों पर फैलते हुए काले धब्बे।"
            }
        },

        "Maize": {
            "problem": {
                "English": "Fall armyworm, stem borer and leaf diseases",
                "हिंदी": "फॉल आर्मीवर्म, तना छेदक और पत्ती रोग"
            },
            "symptoms": {
                "English": "Holes in leaves, damaged central leaves and insect feeding marks.",
                "हिंदी": "पत्तियों में छेद, बीच की पत्तियों का खराब होना और कीट के खाने के निशान।"
            }
        },

        "Chana": {
            "problem": {
                "English": "Gram pod borer, aphids and wilt disease",
                "हिंदी": "चना फली छेदक, माहू और उकठा रोग"
            },
            "symptoms": {
                "English": "Damaged pods, small insects and plants suddenly drying or wilting.",
                "हिंदी": "फलियों में नुकसान, छोटे कीट और पौधों का अचानक सूखना या मुरझाना।"
            }
        },

        "Mustard": {
            "problem": {
                "English": "Aphids, white rust and Alternaria blight",
                "हिंदी": "माहू, सफेद रतुआ और अल्टरनेरिया झुलसा"
            },
            "symptoms": {
                "English": "Small insects on shoots, white patches and dark leaf spots.",
                "हिंदी": "नई टहनियों पर छोटे कीट, सफेद धब्बे और पत्तियों पर गहरे धब्बे।"
            }
        },

        "Sugarcane": {
            "problem": {
                "English": "Early shoot borer, top borer and red rot",
                "हिंदी": "प्रारंभिक तना छेदक, शीर्ष छेदक और लाल सड़न"
            },
            "symptoms": {
                "English": "Dry shoots, holes in stems and reddish discoloration inside the stem.",
                "हिंदी": "टहनियों का सूखना, तने में छेद और तने के अंदर लाल रंग का दिखाई देना।"
            }
        },

        "Tomato": {
            "problem": {
                "English": "Fruit borer, whitefly and early blight",
                "हिंदी": "फल छेदक, सफेद मक्खी और अगेती झुलसा"
            },
            "symptoms": {
                "English": "Holes in fruits, small white insects and dark spots on older leaves.",
                "हिंदी": "फलों में छेद, छोटे सफेद कीट और पुरानी पत्तियों पर गहरे धब्बे।"
            }
        },

        "Onion": {
            "problem": {
                "English": "Thrips, onion fly and purple blotch",
                "हिंदी": "थ्रिप्स, प्याज मक्खी और बैंगनी धब्बा रोग"
            },
            "symptoms": {
                "English": "Silvery patches on leaves, damaged leaves and purple-colored spots.",
                "हिंदी": "पत्तियों पर चांदी जैसे धब्बे, पत्तियों का खराब होना और बैंगनी रंग के धब्बे।"
            }
        },

        "Carrot": {
            "problem": {
                "English": "Aphids, carrot rust fly and leaf diseases",
                "हिंदी": "माहू, गाजर रस्ट फ्लाई और पत्ती रोग"
            },
            "symptoms": {
                "English": "Small insects, damaged roots and yellow or spotted leaves.",
                "हिंदी": "छोटे कीट, जड़ों में नुकसान और पीली या धब्बेदार पत्तियां।"
            }
        },

        "Bottle Gourd": {
            "problem": {
                "English": "Fruit fly, aphids and powdery mildew",
                "हिंदी": "फल मक्खी, माहू और चूर्णिल आसिता"
            },
            "symptoms": {
                "English": "Damaged fruits, small insects and white powder-like patches on leaves.",
                "हिंदी": "फलों में नुकसान, छोटे कीट और पत्तियों पर सफेद पाउडर जैसे धब्बे।"
            }
        },

        "Cauliflower": {
            "problem": {
                "English": "Cabbage butterfly, aphids and downy mildew",
                "हिंदी": "पत्ती खाने वाली इल्ली, माहू और डाउनी मिल्ड्यू"
            },
            "symptoms": {
                "English": "Holes in leaves, small insects and pale or damaged leaves.",
                "हिंदी": "पत्तियों में छेद, छोटे कीट और पीली या खराब पत्तियां।"
            }
        },

        "Cabbage": {
            "problem": {
                "English": "Diamondback moth, aphids and cabbage butterfly",
                "हिंदी": "डायमंडबैक मॉथ, माहू और पत्तागोभी तितली"
            },
            "symptoms": {
                "English": "Small holes in leaves, caterpillars and insects under leaves.",
                "हिंदी": "पत्तियों में छोटे छेद, इल्ली और पत्तियों के नीचे कीट।"
            }
        },

        "Brinjal": {
            "problem": {
                "English": "Shoot and fruit borer, aphids and mites",
                "हिंदी": "तना एवं फल छेदक, माहू और माइट्स"
            },
            "symptoms": {
                "English": "Holes in shoots or fruits, wilting shoots and small insects on leaves.",
                "हिंदी": "नई टहनियों या फलों में छेद, टहनियों का मुरझाना और पत्तियों पर छोटे कीट।"
            }
        },

        "Okra": {
            "problem": {
                "English": "Jassids, whitefly, fruit borer and yellow vein mosaic",
                "हिंदी": "जैसिड, सफेद मक्खी, फल छेदक और पीला शिरा मोजेक"
            },
            "symptoms": {
                "English": "Yellowing leaf edges, insects under leaves, damaged fruits and yellow veins.",
                "हिंदी": "पत्तियों के किनारों का पीला होना, पत्तियों के नीचे कीट, खराब फल और पीली नसें।"
            }
        },

        "Peas": {
            "problem": {
                "English": "Aphids, pod borer and powdery mildew",
                "हिंदी": "माहू, फली छेदक और चूर्णिल आसिता"
            },
            "symptoms": {
                "English": "Small insects, damaged pods and white powder-like growth on leaves.",
                "हिंदी": "छोटे कीट, फलियों में नुकसान और पत्तियों पर सफेद पाउडर जैसा पदार्थ।"
            }
        },

        "Cotton": {
            "problem": {
                "English": "Bollworms, aphids, whitefly and other sucking pests",
                "हिंदी": "बॉलवर्म, माहू, सफेद मक्खी और अन्य रस चूसक कीट"
            },
            "symptoms": {
                "English": "Damaged buds or bolls, curled leaves and insects on the underside of leaves.",
                "हिंदी": "कलियों या टिंडों में नुकसान, मुड़ी हुई पत्तियां और पत्तियों के नीचे कीट।"
            }
        },

        "Bajra": {
            "problem": {
                "English": "Shoot fly, stem borer and downy mildew",
                "हिंदी": "शूट फ्लाई, तना छेदक और डाउनी मिल्ड्यू"
            },
            "symptoms": {
                "English": "Dry central shoots, stem damage and pale or abnormal leaves.",
                "हिंदी": "बीच की टहनियों का सूखना, तने में नुकसान और पीली या असामान्य पत्तियां।"
            }
        },

        "Groundnut": {
            "problem": {
                "English": "Leaf miner, aphids and leaf spot disease",
                "हिंदी": "लीफ माइनर, माहू और पत्ती धब्बा रोग"
            },
            "symptoms": {
                "English": "Leaf tunnels, small insects and brown spots on leaves.",
                "हिंदी": "पत्तियों में सुरंग जैसे निशान, छोटे कीट और पत्तियों पर भूरे धब्बे।"
            }
        },

        "Soybean": {
            "problem": {
                "English": "Stem fly, girdle beetle and leaf-eating insects",
                "हिंदी": "तना मक्खी, गर्डल बीटल और पत्ती खाने वाले कीट"
            },
            "symptoms": {
                "English": "Stem damage, girdling marks and holes or feeding damage on leaves.",
                "हिंदी": "तने में नुकसान, तने पर घेरे जैसे निशान और पत्तियों में छेद या खाने के निशान।"
            }
        }
    }

    st.subheader(text[language]["pest_result"])

    pest_text = {
        "English": {
            "common": "Common problems for",
            "look": "What should you look for?",
            "prevention": "Basic Prevention",
            "check": "• Check leaves, stems and fruits regularly.",
            "remove": "• Remove badly affected plant parts when appropriate.",
            "clean": "• Keep the field clean and maintain proper spacing.",
            "pesticide": "• Avoid unnecessary pesticide use.",
            "warning": "These are general symptoms and prevention tips. This feature does not diagnose a crop from a photo.",
            "serious": "For serious infestation, consult a local agriculture expert before using pesticides."
        },
        "हिंदी": {
            "common": "चुनी गई फसल की सामान्य समस्याएं:",
            "look": "क्या देखें?",
            "prevention": "बचाव के आसान तरीके",
            "check": "• पत्तियों, तनों और फलों की नियमित जांच करें।",
            "remove": "• जरूरत होने पर बहुत अधिक प्रभावित हिस्सों को हटा दें।",
            "clean": "• खेत को साफ रखें और पौधों के बीच उचित दूरी रखें।",
            "pesticide": "• बिना जरूरत कीटनाशक का उपयोग न करें।",
            "warning": "ये सामान्य लक्षण और बचाव की जानकारी हैं। यह सुविधा तस्वीर से फसल के रोग की पहचान नहीं करती।",
            "serious": "गंभीर संक्रमण की स्थिति में कीटनाशक का उपयोग करने से पहले स्थानीय कृषि विशेषज्ञ से सलाह लें।"
        }
   }

    p = pest_text[language]

    st.write(p["common"], selected_crop)
    st.info(pest_data[crop]["problem"][language])

    st.subheader(p["look"])
    st.write(pest_data[crop]["symptoms"][language])

    st.subheader(p["prevention"])
    st.write(p["check"])
    st.write(p["remove"])
    st.write(p["clean"])
    st.write(p["pesticide"])
    st.warning(p["warning"])
    st.caption(p["serious"])
                
if option == "Pest & Disease Detection":
    show_pest_detection()      
    
    
    

def show_yield_prediction():
    
    st.subheader(text[language]["yield_prediction"])
    st.write(text[language]["yield_desc"])

    
    crop_names = {
        crop_data["Wheat"]["name"][language]: "Wheat",
        crop_data["Rice"]["name"][language]: "Rice",
        crop_data["Potato"]["name"][language]: "Potato",
        crop_data["Maize"]["name"][language]: "Maize",
        crop_data["Chana"]["name"][language]: "Chana",
        crop_data["Mustard"]["name"][language]: "Mustard",
        crop_data["Sugarcane"]["name"][language]: "Sugarcane",
        crop_data["Tomato"]["name"][language]: "Tomato",
        crop_data["Onion"]["name"][language]: "Onion",
        crop_data["Carrot"]["name"][language]: "Carrot",
        crop_data["Bottle Gourd"]["name"][language]: "Bottle Gourd",
        crop_data["Cauliflower"]["name"][language]: "Cauliflower",
        crop_data["Cabbage"]["name"][language]: "Cabbage",
        crop_data["Brinjal"]["name"][language]: "Brinjal",
        crop_data["Okra"]["name"][language]: "Okra",
        crop_data["Peas"]["name"][language]: "Peas",
        crop_data["Cotton"]["name"][language]: "Cotton",
        crop_data["Bajra"]["name"][language]: "Bajra",
        crop_data["Groundnut"]["name"][language]: "Groundnut",
        crop_data["Soybean"]["name"][language]: "Soybean"
    }

    selected_crop = st.selectbox(
        text[language]["select_crop_yield"],
        list(crop_names.keys())
    )

    crop = crop_names[selected_crop]

    yield_text = {
        "English": {
            "intro": "Enter the basic conditions of your farm to get an approximate yield estimate.",
            "area_help": "Enter your farm area in hectares.",
            "temperature_help": "Enter the average temperature during the crop growing period.",
            "rainfall_help": "Enter the approximate rainfall received during the crop season.",
            "soil_help": "Choose the soil type that is closest to your farm soil.",
            "fertilizer_help": "Choose the fertilizer use level that is closest to your farm practice."
        },
        "हिंदी": {
            "intro": "अपनी खेती की सामान्य जानकारी भरें और अनुमानित उपज प्राप्त करें।",
            "area_help": "अपने खेत का क्षेत्रफल हेक्टेयर में दर्ज करें।",
            "temperature_help": "फसल की बढ़वार के दौरान औसत तापमान दर्ज करें।",
            "rainfall_help": "फसल के मौसम में हुई लगभग वर्षा दर्ज करें।",
            "soil_help": "अपने खेत की मिट्टी के सबसे करीब वाला प्रकार चुनें।",
            "fertilizer_help": "अपने खेत में उपयोग होने वाली उर्वरक मात्रा के सबसे करीब वाला स्तर चुनें।"
        }
    }

    st.write(yield_text[language]["intro"])


    area = st.number_input(
        text[language]["area"],
        min_value=0.1,
        max_value=1000.0,
        value=1.0,
        step=0.1,
        help=yield_text[language]["area_help"]
    )

    temperature = st.number_input(
        text[language]["temperature_yield"],
        min_value=0.0,
        max_value=50.0,
        value=25.0,
        step=0.5,
        help=yield_text[language]["temperature_help"]
    )

    rainfall = st.number_input(
        text[language]["rainfall_yield"],
        min_value=0.0,
        max_value=3000.0,
        value=600.0,
        step=10.0,
        help=yield_text[language]["rainfall_help"]
    )

    soil = st.selectbox(
    text[language]["soil_yield"],
    [
        "Loamy Soil",
        "Sandy Soil",
        "Clay Soil",
        "Black Soil"
    ],
    help=yield_text[language]["soil_help"]
    )

    fertilizer = st.selectbox(
        text[language]["fertilizer_yield"],
        [
            "Low",
            "Medium",
            "High"
        ],
        help=yield_text[language]["fertilizer_help"]
    )

    if st.button(
        text[language]["predict_yield"],
        use_container_width=True
    ):

        
        base_yield = {
            "Wheat": 3.5,
            "Rice": 4.0,
            "Potato": 20.0,
            "Maize": 4.0,
            "Chana": 2.0,
            "Mustard": 1.5,
            "Sugarcane": 75.0,
            "Tomato": 30.0,
            "Onion": 25.0,
            "Carrot": 25.0,
            "Bottle Gourd": 20.0,
            "Cauliflower": 20.0,
            "Cabbage": 25.0,
            "Brinjal": 25.0,
            "Okra": 10.0,
            "Peas": 8.0,
            "Cotton": 2.0,
            "Bajra": 2.0,
            "Groundnut": 2.5,
            "Soybean": 2.5
        }

        estimated_yield = base_yield[crop]

        
        if soil == "Loamy Soil":
            estimated_yield = estimated_yield * 1.10

        elif soil == "Black Soil":
            if crop in ["Cotton", "Soybean", "Wheat", "Chana"]:
                estimated_yield = estimated_yield * 1.10
            else:
                estimated_yield = estimated_yield * 1.05

        elif soil == "Sandy Soil":
            if crop in ["Groundnut", "Carrot", "Bajra"]:
                estimated_yield = estimated_yield * 1.08
            else:
                estimated_yield = estimated_yield * 0.95

        elif soil == "Clay Soil":
            if crop == "Rice":
                estimated_yield = estimated_yield * 1.10
            else:
                estimated_yield = estimated_yield * 0.95

        
        if fertilizer == "High":
            estimated_yield = estimated_yield * 1.10

        elif fertilizer == "Medium":
            estimated_yield = estimated_yield * 1.05

        else:
            estimated_yield = estimated_yield * 0.90

        
        if crop == "Rice":

            if rainfall < 800:
                estimated_yield = estimated_yield * 0.85

            elif rainfall > 2500:
                estimated_yield = estimated_yield * 0.90

        elif crop in ["Bajra", "Groundnut", "Cotton"]:

            if rainfall < 400:
                estimated_yield = estimated_yield * 0.85

            elif rainfall > 1500:
                estimated_yield = estimated_yield * 0.95

        else:

            if rainfall < 300:
                estimated_yield = estimated_yield * 0.85

            elif rainfall > 2000:
                estimated_yield = estimated_yield * 0.90

        
        suitable_temperature = {
            "Wheat": (15, 25),
            "Rice": (20, 35),
            "Potato": (15, 25),
            "Maize": (20, 30),
            "Chana": (15, 25),
            "Mustard": (13, 25),
            "Sugarcane": (20, 35),
            "Tomato": (18, 27),
            "Onion": (13, 25),
            "Carrot": (15, 25),
            "Bottle Gourd": (25, 35),
            "Cauliflower": (15, 25),
            "Cabbage": (15, 25),
            "Brinjal": (22, 30),
            "Okra": (24, 32),
            "Peas": (10, 25),
            "Cotton": (21, 30),
            "Bajra": (25, 35),
            "Groundnut": (25, 30),
            "Soybean": (20, 30)
        }

        min_temp, max_temp = suitable_temperature[crop]

        if temperature < min_temp or temperature > max_temp:
            estimated_yield = estimated_yield * 0.85

        
        total_yield = estimated_yield * area

        
        if estimated_yield < base_yield[crop] * 0.90:
            yield_status = "Low"

        elif estimated_yield < base_yield[crop] * 1.05:
            yield_status = "Medium"

        else:
            yield_status = "High"

        
        if language == "English":

            st.subheader("Prediction Result")

            if yield_status == "Low":
                st.warning("Low Yield Expected")

            elif yield_status == "Medium":
                st.info("Medium Yield Expected")

            else:
                st.success("High Yield Expected")

            col1, col2 = st.columns(2)

            with col1:
                st.metric(
                    "Estimated Yield",
                    f"{estimated_yield:.2f} tonnes/ha"
                )

            with col2:
                st.metric(
                    "Total Production",
                    f"{total_yield:.2f} tonnes"
                )

            st.write("### Why this prediction?")

            st.write(
                "This estimate is calculated from the selected crop, "
                "farm area, temperature, rainfall, soil type and fertilizer usage."
            )

            st.caption(
                "This is a basic estimate, not a machine-learning prediction. "
                "Actual production can vary with seed quality, pests, irrigation, "
                "weather and farming practices."
            )

        else:

            st.subheader("अनुमान का परिणाम")

            if yield_status == "Low":
                st.warning("कम उपज की संभावना")

            elif yield_status == "Medium":
                st.info("मध्यम उपज की संभावना")

            else:
                st.success("अच्छी उपज की संभावना")

            col1, col2 = st.columns(2)

            with col1:
                st.metric(
                    "अनुमानित उपज",
                    f"{estimated_yield:.2f} टन/हेक्टेयर"
                )

            with col2:
                st.metric(
                    "कुल उत्पादन",
                    f"{total_yield:.2f} टन"
                )

            st.write("### यह अनुमान क्यों?")

            st.write(
                "यह अनुमान चुनी गई फसल, खेत का क्षेत्रफल, "
                "तापमान, वर्षा, मिट्टी और उर्वरक के उपयोग "
                "के आधार पर लगाया गया है।"
            )

        st.info(
            text[language]["yield_note"]
        )
       
if option == "Yield Prediction":
    show_yield_prediction()                    