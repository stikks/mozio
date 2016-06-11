# coding=utf-8
"""
Django settings for mozio project.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.6/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os

BASE_DIR = os.path.dirname(os.path.dirname(__file__))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.6/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'y523x-9_!*n)jj!s@r@k1%j=59p64&5pnqfxx=f073&dgc6d7e'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.gis',
    'app',
    'rest_framework',
    'djgeojson',
    'rest_framework_docs',
    'rest_framework_swagger',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'mozio.urls'

WSGI_APPLICATION = 'mozio.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.6/ref/settings/#databases


# Internationalization
# https://docs.djangoproject.com/en/1.6/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.6/howto/static-files/
STATIC_ROOT = os.path.join(BASE_DIR, 'static')


STATIC_URL = '/static/'

REST_FRAMEWORK = {
    # Use Django's standard `django.contrib.auth` permissions,
    # or allow read-only access for unauthenticated users.
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.AllowAny'
    ],
    'PAGE_SIZE': 20,
    # 'TEST_REQUEST_RENDERER_CLASSES': (
    #     'rest_framework.renderers.MultiPartRenderer',
    #     'rest_framework.renderers.JSONRenderer',
    #     'rest_framework.renderers.TemplateHTMLRenderer'
    # ),
    'TEST_REQUEST_DEFAULT_FORMAT': 'json'
}

REST_FRAMEWORK_DOCS = {
    'HIDE_DOCS': os.environ.get('HIDE_DRFDOCS', False)
}

LANGUAGES = [
  {
    "code": "ab",
    "name": "Abkhaz",
  },
  {
    "code": "aa",
    "name": "Afar",
  },
  {
    "code": "af",
    "name": "Afrikaans",
  },
  {
    "code": "ak",
    "name": "Akan",
  },
  {
    "code": "sq",
    "name": "Albanian",
  },
  {
    "code": "am",
    "name": "Amharic",
  },
  {
    "code": "ar",
    "name": "Arabic",
  },
  {
    "code": "an",
    "name": "Aragonese",
  },
  {
    "code": "hy",
    "name": "Armenian",
  },
  {
    "code": "as",
    "name": "Assamese",
  },
  {
    "code": "av",
    "name": "Avaric",
  },
  {
    "code": "ae",
    "name": "Avestan",
  },
  {
    "code": "ay",
    "name": "Aymara",
  },
  {
    "code": "az",
    "name": "Azerbaijani",
  },
  {
    "code": "bm",
    "name": "Bambara",
  },
  {
    "code": "ba",
    "name": "Bashkir",
  },
  {
    "code": "eu",
    "name": "Basque"
  },
  {
    "code": "be",
    "name": "Belarusian",
  },
  {
    "code": "bn",
    "name": "Bengali",
  },
  {
    "code": "bh",
    "name": "Bihari",
  },
  {
    "code": "bi",
    "name": "Bislama",
  },
  {
    "code": "bs",
    "name": "Bosnian",
  },
  {
    "code": "br",
    "name": "Breton",
  },
  {
    "code": "bg",
    "name": "Bulgarian",
  },
  {
    "code": "my",
    "name": "Burmese",
  },
  {
    "code": "ca",
    "name": "Catalan",
  },
  {
    "code": "ch",
    "name": "Chamorro",
  },
  {
    "code": "ce",
    "name": "Chechen",
  },
  {
    "code": "ny",
    "name": "Chichewa",
  },
  {
    "code": "zh",
    "name": "Chinese",
  },
  {
    "code": "cv",
    "name": "Chuvash",
  },
  {
    "code": "kw",
    "name": "Cornish",
  },
  {
    "code": "co",
    "name": "Corsican",
  },
  {
    "code": "cr",
    "name": "Cree",
  },
  {
    "code": "hr",
    "name": "Croatian",
  },
  {
    "code": "cs",
    "name": "Czech",
  },
  {
    "code": "da",
    "name": "Danish",
  },
  {
    "code": "dv",
    "name": "Divehi;",
  },
  {
    "code": "nl",
    "name": "Dutch",
  },
  {
    "code": "en",
    "name": "English",
  },
  {
    "code": "eo",
    "name": "Esperanto",
  },
  {
    "code": "et",
    "name": "Estonian",
  },
  {
    "code": "ee",
    "name": "Ewe",
  },
  {
    "code": "fo",
    "name": "Faroese",
  },
  {
    "code": "fj",
    "name": "Fijian",
  },
  {
    "code": "fi",
    "name": "Finnish",
  },
  {
    "code": "fr",
    "name": "French",
  },
  {
    "code": "ff",
    "name": "Fula",
  },
  {
    "code": "gl",
    "name": "Galician",
  },
  {
    "code": "ka",
    "name": "Georgian",
  },
  {
    "code": "de",
    "name": "German",
  },
  {
    "code": "el",
    "name": "Greek",
  },
  {
    "code": "gn",
    "name": "Guarani",
  },
  {
    "code": "gu",
    "name": "Gujarati",
  },
  {
    "code": "ht",
    "name": "Haitian",
  },
  {
    "code": "ha",
    "name": "Hausa",
  },
  {
    "code": "he",
    "name": "Hebrew",
  },
  {
    "code": "hz",
    "name": "Herero",
  },
  {
    "code": "hi",
    "name": "Hindi",
  },
  {
    "code": "ho",
    "name": "Hiri Motu",
  },
  {
    "code": "hu",
    "name": "Hungarian",
  },
  {
    "code": "ia",
    "name": "Interlingua",
  },
  {
    "code": "id",
    "name": "Indonesian",
  },
  {
    "code": "ie",
    "name": "Interlingue",
  },
  {
    "code": "ga",
    "name": "Irish",
  },
  {
    "code": "ig",
    "name": "Igbo",
  },
  {
    "code": "ik",
    "name": "Inupiaq",
  },
  {
    "code": "io",
    "name": "Ido",
  },
  {
    "code": "is",
    "name": "Icelandic",
  },
  {
    "code": "it",
    "name": "Italian",
  },
  {
    "code": "iu",
    "name": "Inuktitut",
  },
  {
    "code": "ja",
    "name": "Japanese",
  },
  {
    "code": "jv",
    "name": "Javanese",
  },
  {
    "code": "kl",
    "name": "Kalaallisut",
  },
  {
    "code": "kn",
    "name": "Kannada",
  },
  {
    "code": "kr",
    "name": "Kanuri",
  },
  {
    "code": "ks",
    "name": "Kashmiri",
  },
  {
    "code": "kk",
    "name": "Kazakh",
  },
  {
    "code": "km",
    "name": "Khmer",
  },
  {
    "code": "ki",
    "name": "Kikuyu",
  },
  {
    "code": "rw",
    "name": "Kinyarwanda",
  },
  {
    "code": "ky",
    "name": "Kirghiz",
  },
  {
    "code": "kv",
    "name": "Komi",
  },
  {
    "code": "kg",
    "name": "Kongo",
  },
  {
    "code": "ko",
    "name": "Korean",
  },
  {
    "code": "ku",
    "name": "Kurdish",
  },
  {
    "code": "kj",
    "name": "Kwanyama",
  },
  {
    "code": "la",
    "name": "Latin",
  },
  {
    "code": "lb",
    "name": "Luxembourgish",
  },
  {
    "code": "lg",
    "name": "Luganda",
  },
  {
    "code": "li",
    "name": "Limburgish",
  },
  {
    "code": "ln",
    "name": "Lingala",
  },
  {
    "code": "lo",
    "name": "Lao",
  },
  {
    "code": "lt",
    "name": "Lithuanian",
  },
  {
    "code": "lu",
    "name": "Luba-Katanga",
  },
  {
    "code": "lv",
    "name": "Latvian",
  },
  {
    "code": "gv",
    "name": "Manx",
  },
  {
    "code": "mk",
    "name": "Macedonian",
  },
  {
    "code": "mg",
    "name": "Malagasy",
  },
  {
    "code": "ms",
    "name": "Malay",
  },
  {
    "code": "ml",
    "name": "Malayalam",
  },
  {
    "code": "mt",
    "name": "Maltese",
  },
  {
    "code": "mi",
    "name": "Maori",
  },
  {
    "code": "mr",
    "name": "Marathi",
  },
  {
    "code": "mh",
    "name": "Marshallese",
  },
  {
    "code": "mn",
    "name": "Mongolian",
  },
  {
    "code": "na",
    "name": "Nauru",
  },
  {
    "code": "nv",
    "name": "Navajo",
  },
  {
    "code": "nb",
    "name": "Norwegian Bokmal",
  },
  {
    "code": "nd",
    "name": "North Ndebele",
  },
  {
    "code": "ne",
    "name": "Nepali",
  },
  {
    "code": "ng",
    "name": "Ndonga",
  },
  {
    "code": "nn",
    "name": "Norwegian Nynorsk",
  },
  {
    "code": "no",
    "name": "Norwegian",
  },
  {
    "code": "ii",
    "name": "Nuosu",
  },
  {
    "code": "nr",
    "name": "South Ndebele",
  },
  {
    "code": "oc",
    "name": "Occitan",
    "nativeName": "Occitan"
  },
  {
    "code": "oj",
    "name": "Ojibwe, Ojibwa",
  },
  {
    "code": "cu",
    "name": "Old Church Slavonic",
  },
  {
    "code": "om",
    "name": "Oromo",
  },
  {
    "code": "or",
    "name": "Oriya",
  },
  {
    "code": "os",
    "name": "Ossetian",
  },
  {
    "code": "pa",
    "name": "Punjabi",
  },
  {
    "code": "pi",
    "name": "Pali",
  },
  {
    "code": "fa",
    "name": "Persian",
  },
  {
    "code": "pl",
    "name": "Polish",
  },
  {
    "code": "ps",
    "name": "Pashto",
  },
  {
    "code": "pt",
    "name": "Portuguese",
  },
  {
    "code": "qu",
    "name": "Quechua",
  },
  {
    "code": "rm",
    "name": "Romansh",
  },
  {
    "code": "rn",
    "name": "Kirundi",
  },
  {
    "code": "ro",
    "name": "Romanian",
  },
  {
    "code": "ru",
    "name": "Russian",
  },
  {
    "code": "sa",
    "name": "Sanskrit",
  },
  {
    "code": "sc",
    "name": "Sardinian",
  },
  {
    "code": "sd",
    "name": "Sindhi",
  },
  {
    "code": "se",
    "name": "Northern Sami",
  },
  {
    "code": "sm",
    "name": "Samoan",
  },
  {
    "code": "sg",
    "name": "Sango",
  },
  {
    "code": "sr",
    "name": "Serbian",
  },
  {
    "code": "gd",
    "name": "Scottish Gaelic",
  },
  {
    "code": "sn",
    "name": "Shona",
  },
  {
    "code": "si",
    "name": "Sinhala",
  },
  {
    "code": "sk",
    "name": "Slovak",
  },
  {
    "code": "sl",
    "name": "Slovene",
  },
  {
    "code": "so",
    "name": "Somali",
  },
  {
    "code": "st",
    "name": "Southern Sotho"
  },
  {
    "code": "es",
    "name": "Spanish"
  },
  {
    "code": "su",
    "name": "Sundanese",
  },
  {
    "code": "sw",
    "name": "Swahili",
  },
  {
    "code": "ss",
    "name": "Swati",
  },
  {
    "code": "sv",
    "name": "Swedish",
  },
  {
    "code": "ta",
    "name": "Tamil",
  },
  {
    "code": "te",
    "name": "Telugu",
  },
  {
    "code": "tg",
    "name": "Tajik",
  },
  {
    "code": "th",
    "name": "Thai",
  },
  {
    "code": "ti",
    "name": "Tigrinya",
  },
  {
    "code": "bo",
    "name": "Tibetan",
  },
  {
    "code": "tk",
    "name": "Turkmen",
  },
  {
    "code": "tl",
    "name": "Tagalog",
  },
  {
    "code": "tn",
    "name": "Tswana",
  },
  {
    "code": "to",
    "name": "Tonga (Tonga Islands)",
  },
  {
    "code": "tr",
    "name": "Turkish",
  },
  {
    "code": "ts",
    "name": "Tsonga",
  },
  {
    "code": "tt",
    "name": "Tatar",
  },
  {
    "code": "tw",
    "name": "Twi",
  },
  {
    "code": "ty",
    "name": "Tahitian",
  },
  {
    "code": "ug",
    "name": "Uighur",
  },
  {
    "code": "uk",
    "name": "Ukrainian",
  },
  {
    "code": "ur",
    "name": "Urdu",
  },
  {
    "code": "uz",
    "name": "Uzbek",
  },
  {
    "code": "ve",
    "name": "Venda",
  },
  {
    "code": "vi",
    "name": "Vietnamese",
  },
  {
    "code": "vo",
    "name": "Volapuk",
  },
  {
    "code": "wa",
    "name": "Walloon",
  },
  {
    "code": "cy",
    "name": "Welsh",
  },
  {
    "code": "wo",
    "name": "Wolof",
  },
  {
    "code": "fy",
    "name": "Western Frisian",
  },
  {
    "code": "xh",
    "name": "Xhosa",
  },
  {
    "code": "yi",
    "name": "Yiddish",
  },
  {
    "code": "yo",
    "name": "Yoruba",
  },
  {
    "code": "za",
    "name": "Zhuang",
  }
]

CURRENCIES = [
  {"code":"AED","symbol":"\u062f.\u0625;","name":"UAE dirham"},
  {"code":"AFN","symbol":"Afs","name":"Afghan afghani"},
  {"code":"ALL","symbol":"L","name":"Albanian lek"},
  {"code":"AMD","symbol":"AMD","name":"Armenian dram"},
  {"code":"ANG","symbol":"NA\u0192","name":"Netherlands Antillean gulden"},
  {"code":"AOA","symbol":"Kz","name":"Angolan kwanza"},
  {"code":"ARS","symbol":"$","name":"Argentine peso"},
  {"code":"AUD","symbol":"$","name":"Australian dollar"},
  {"code":"AWG","symbol":"\u0192","name":"Aruban florin"},
  {"code":"AZN","symbol":"AZN","name":"Azerbaijani manat"},
  {"code":"BAM","symbol":"KM","name":"Bosnia and Herzegovina konvertibilna marka"},
  {"code":"BBD","symbol":"Bds$","name":"Barbadian dollar"},
  {"code":"BDT","symbol":"\u09f3","name":"Bangladeshi taka"},
  {"code":"BGN","symbol":"BGN","name":"Bulgarian lev"},
  {"code":"BHD","symbol":".\u062f.\u0628","name":"Bahraini dinar"},
  {"code":"BIF","symbol":"FBu","name":"Burundi franc"},
  {"code":"BMD","symbol":"BD$","name":"Bermudian dollar"},
  {"code":"BND","symbol":"B$","name":"Brunei dollar"},
  {"code":"BOB","symbol":"Bs.","name":"Bolivian boliviano"},
  {"code":"BRL","symbol":"R$","name":"Brazilian real"},
  {"code":"BSD","symbol":"B$","name":"Bahamian dollar"},
  {"code":"BTN","symbol":"Nu.","name":"Bhutanese ngultrum"},
  {"code":"BWP","symbol":"P","name":"Botswana pula"},
  {"code":"BYR","symbol":"Br","name":"Belarusian ruble"},
  {"code":"BZD","symbol":"BZ$","name":"Belize dollar"},
  {"code":"CAD","symbol":"$","name":"Canadian dollar"},
  {"code":"CDF","symbol":"F","name":"Congolese franc"},
  {"code":"CHF","symbol":"Fr.","name":"Swiss franc"},
  {"code":"CLP","symbol":"$","name":"Chilean peso"},
  {"code":"CNY","symbol":"\u00a5","name":"Chinese/Yuan renminbi"},
  {"code":"COP","symbol":"Col$","name":"Colombian peso"},
  {"code":"CRC","symbol":"\u20a1","name":"Costa Rican colon"},
  {"code":"CUC","symbol":"$","name":"Cuban peso"},
  {"code":"CVE","symbol":"Esc","name":"Cape Verdean escudo"},
  {"code":"CZK","symbol":"K\u010d","name":"Czech koruna"},
  {"code":"DJF","symbol":"Fdj","name":"Djiboutian franc"},
  {"code":"DKK","symbol":"Kr","name":"Danish krone"},
  {"code":"DOP","symbol":"RD$","name":"Dominican peso"},
  {"code":"DZD","symbol":"\u062f.\u062c","name":"Algerian dinar"},
  {"code":"EEK","symbol":"KR","name":"Estonian kroon"},
  {"code":"EGP","symbol":"\u00a3","name":"Egyptian pound"},
  {"code":"ERN","symbol":"Nfa","name":"Eritrean nakfa"},
  {"code":"ETB","symbol":"Br","name":"Ethiopian birr"},
  {"code":"EUR","symbol":"\u20ac","name":"European Euro"},
  {"code":"FJD","symbol":"FJ$","name":"Fijian dollar"},
  {"code":"FKP","symbol":"\u00a3","name":"Falkland Islands pound"},
  {"code":"GBP","symbol":"\u00a3","name":"British pound"},
  {"code":"GEL","symbol":"GEL","name":"Georgian lari"},
  {"code":"GHS","symbol":"GH\u20b5","name":"Ghanaian cedi"},
  {"code":"GIP","symbol":"\u00a3","name":"Gibraltar pound"},
  {"code":"GMD","symbol":"D","name":"Gambian dalasi"},
  {"code":"GNF","symbol":"FG","name":"Guinean franc"},
  {"code":"GQE","symbol":"CFA","name":"Central African CFA franc"},
  {"code":"GTQ","symbol":"Q","name":"Guatemalan quetzal"},
  {"code":"GYD","symbol":"GY$","name":"Guyanese dollar"},
  {"code":"HKD","symbol":"HK$","name":"Hong Kong dollar"},
  {"code":"HNL","symbol":"L","name":"Honduran lempira"},
  {"code":"HRK","symbol":"kn","name":"Croatian kuna"},
  {"code":"HTG","symbol":"G","name":"Haitian gourde"},
  {"code":"HUF","symbol":"Ft","name":"Hungarian forint"},
  {"code":"IDR","symbol":"Rp","name":"Indonesian rupiah"},
  {"code":"ILS","symbol":"\u20aa","name":"Israeli new sheqel"},
  {"code":"INR","symbol":"\u20B9","name":"Indian rupee"},
  {"code":"IQD","symbol":"\u062f.\u0639","name":"Iraqi dinar"},
  {"code":"IRR","symbol":"IRR","name":"Iranian rial"},
  {"code":"ISK","symbol":"kr","name":"Icelandic kr\u00f3na"},
  {"code":"JMD","symbol":"J$","name":"Jamaican dollar"},
  {"code":"JOD","symbol":"JOD","name":"Jordanian dinar"},
  {"code":"JPY","symbol":"\u00a5","name":"Japanese yen"},
  {"code":"KES","symbol":"KSh","name":"Kenyan shilling"},
  {"code":"KGS","symbol":"\u0441\u043e\u043c","name":"Kyrgyzstani som"},
  {"code":"KHR","symbol":"\u17db","name":"Cambodian riel"},
  {"code":"KMF","symbol":"KMF","name":"Comorian franc"},
  {"code":"KPW","symbol":"W","name":"North Korean won"},
  {"code":"KRW","symbol":"W","name":"South Korean won"},
  {"code":"KWD","symbol":"KWD","name":"Kuwaiti dinar"},
  {"code":"KYD","symbol":"KY$","name":"Cayman Islands dollar"},
  {"code":"KZT","symbol":"T","name":"Kazakhstani tenge"},
  {"code":"LAK","symbol":"KN","name":"Lao kip"},
  {"code":"LBP","symbol":"\u00a3","name":"Lebanese lira"},
  {"code":"LKR","symbol":"Rs","name":"Sri Lankan rupee"},
  {"code":"LRD","symbol":"L$","name":"Liberian dollar"},
  {"code":"LSL","symbol":"M","name":"Lesotho loti"},
  {"code":"LTL","symbol":"Lt","name":"Lithuanian litas"},
  {"code":"LVL","symbol":"Ls","name":"Latvian lats"},
  {"code":"LYD","symbol":"LD","name":"Libyan dinar"},
  {"code":"MAD","symbol":"MAD","name":"Morocodean dirham"},
  {"code":"MDL","symbol":"MDL","name":"Moldovan leu"},
  {"code":"MGA","symbol":"FMG","name":"Malagasy ariary"},
  {"code":"MKD","symbol":"MKD","name":"Macedonian denar"},
  {"code":"MMK","symbol":"K","name":"Myanma kyat"},
  {"code":"MNT","symbol":"\u20ae","name":"Mongolian tugrik"},
  {"code":"MOP","symbol":"P","name":"Macanese pataca"},
  {"code":"MRO","symbol":"UM","name":"Mauritanian ouguiya"},
  {"code":"MUR","symbol":"Rs","name":"Mauritian rupee"},
  {"code":"MVR","symbol":"Rf","name":"Maldivian rufiyaa"},
  {"code":"MWK","symbol":"MK","name":"Malawian kwacha"},
  {"code":"MXN","symbol":"$","name":"Mexican peso"},
  {"code":"MYR","symbol":"RM","name":"Malaysian ringgit"},
  {"code":"MZM","symbol":"MTn","name":"Mozambican metical"},
  {"code":"NAD","symbol":"N$","name":"Namibian dollar"},
  {"code":"NGN","symbol":"\u20a6","name":"Nigerian naira"},
  {"code":"NIO","symbol":"C$","name":"Nicaraguan c\u00f3rdoba"},
  {"code":"NOK","symbol":"kr","name":"Norwegian krone"},
  {"code":"NPR","symbol":"NRs","name":"Nepalese rupee"},
  {"code":"NZD","symbol":"NZ$","name":"New Zealand dollar"},
  {"code":"OMR","symbol":"OMR","name":"Omani rial"},
  {"code":"PAB","symbol":"B./","name":"Panamanian balboa"},
  {"code":"PEN","symbol":"S/.","name":"Peruvian nuevo sol"},
  {"code":"PGK","symbol":"K","name":"Papua New Guinean kina"},
  {"code":"PHP","symbol":"\u20b1","name":"Philippine peso"},
  {"code":"PKR","symbol":"Rs.","name":"Pakistani rupee"},
  {"code":"PLN","symbol":"z\u0142","name":"Polish zloty"},
  {"code":"PYG","symbol":"\u20b2","name":"Paraguayan guarani"},
  {"code":"QAR","symbol":"QR","name":"Qatari riyal"},
  {"code":"RON","symbol":"L","name":"Romanian leu"},
  {"code":"RSD","symbol":"din.","name":"Serbian dinar"},
  {"code":"RUB","symbol":"R","name":"Russian ruble"},
  {"code":"SAR","symbol":"SR","name":"Saudi riyal"},
  {"code":"SBD","symbol":"SI$","name":"Solomon Islands dollar"},
  {"code":"SCR","symbol":"SR","name":"Seychellois rupee"},
  {"code":"SDG","symbol":"SDG","name":"Sudanese pound"},
  {"code":"SEK","symbol":"kr","name":"Swedish krona"},
  {"code":"SGD","symbol":"S$","name":"Singapore dollar"},
  {"code":"SHP","symbol":"\u00a3","name":"Saint Helena pound"},
  {"code":"SLL","symbol":"Le","name":"Sierra Leonean leone"},
  {"code":"SOS","symbol":"Sh.","name":"Somali shilling"},
  {"code":"SRD","symbol":"$","name":"Surinamese dollar"},
  {"code":"SYP","symbol":"LS","name":"Syrian pound"},
  {"code":"SZL","symbol":"E","name":"Swazi lilangeni"},
  {"code":"THB","symbol":"\u0e3f","name":"Thai baht"},
  {"code":"TJS","symbol":"TJS","name":"Tajikistani somoni"},
  {"code":"TMT","symbol":"m","name":"Turkmen manat"},
  {"code":"TND","symbol":"DT","name":"Tunisian dinar"},
  {"code":"TRY","symbol":"TRY","name":"Turkish new lira"},
  {"code":"TTD","symbol":"TT$","name":"Trinidad and Tobago dollar"},
  {"code":"TWD","symbol":"NT$","name":"New Taiwan dollar"},
  {"code":"TZS","symbol":"TZS","name":"Tanzanian shilling"},
  {"code":"UAH","symbol":"UAH","name":"Ukrainian hryvnia"},
  {"code":"UGX","symbol":"USh","name":"Ugandan shilling"},
  {"code":"USD","symbol":"US$","name":"United States dollar"},
  {"code":"UYU","symbol":"$U","name":"Uruguayan peso"},
  {"code":"UZS","symbol":"UZS","name":"Uzbekistani som"},
  {"code":"VEB","symbol":"Bs","name":"Venezuelan bolivar"},
  {"code":"VND","symbol":"\u20ab","name":"Vietnamese dong"},
  {"code":"VUV","symbol":"VT","name":"Vanuatu vatu"},
  {"code":"WST","symbol":"WS$","name":"Samoan tala"},
  {"code":"XAF","symbol":"CFA","name":"Central African CFA franc"},
  {"code":"XCD","symbol":"EC$","name":"East Caribbean dollar"},
  {"code":"XDR","symbol":"SDR","name":"Special Drawing Rights"},
  {"code":"XOF","symbol":"CFA","name":"West African CFA franc"},
  {"code":"XPF","symbol":"F","name":"CFP franc"},
  {"code":"YER","symbol":"YER","name":"Yemeni rial"},
  {"code":"ZAR","symbol":"R","name":"South African rand"},
  {"code":"ZMK","symbol":"ZK","name":"Zambian kwacha"},
  {"code":"ZWR","symbol":"Z$","name":"Zimbabwean dollar"}
]

