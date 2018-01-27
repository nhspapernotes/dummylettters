from reportlab.pdfgen.canvas import Canvas
from reportlab.lib.colors import white, blue
from reportlab.platypus import Paragraph
from reportlab.lib.styles import getSampleStyleSheet
from random import *
from datetime import timedelta, date
import string
import random




def newfilename():
    min_char = 10
    max_char = 20
    allchar = string.ascii_letters + string.digits
    filename = "".join(choice(allchar) for x in range(randint(min_char, max_char)))
    return filename

def randcondtion():
    conditions = ('Asthma',
    'COPD',
    'Type 2 Diabetes',
    'Type 1 Diabetes',
    'Angina',
    'Myocardial infarction',
    'Ischemic heart disease',
    'Pulmonary embolism',
    'Deep vein thrombosis',
    'Fractured neck of femur',
    'Epistaxis',
    'Sepsis ',
    'Community acquired Pneumonia',
    'Hospital acquired pneumonia',
    'UTI ',
    'Alzheimers dementia',
    'Vascular dementia',
    'Aspiration pneumonia',
    'Pancreatitis',
    'Fracture (specify)',
    'Head injury',
    'Haemorrhagic stroke',
    'Ischaemic stroke',
    'Hypertension',
    'Hypercholesterolemia',
    'Hyperthyroidism',
    'Hypothyroidism',
    'Addisons',
    'Cushings syndrome',
    'Rheumatoid arthritis',
    'Osteoporosis',
    'Osteoarthritis',
    'Shingles',
    'Influenza',
    'Depression',
    'Schizophrenia',
    'Bipolar disorder',
    'Epilepsy (specify)',
    'Overdose (specify)',
    'Alcoholic liver disease',
    'Hepatitis (specify)',
    'Hyperkalemia',
    'Hypokalemia',
    'Hypernatraemia',
    'Hyponatremia',
    'Diabetic ketoacidosis',
    'Fall',
    'Dehydration',
    'Acute kidney injury',
    'Chronic kidney disease (specify)',
    'Airway obstruction',
    'Tonsillitis',
    'Quinsy',
    'Otitis externa',
    'Foreign body',
    'Neck lump',
    'Ductal carcinoma of the breast in situ',
    'Abdominal aortic aneurysm',
    'Ischemic bowel',
    'Diverticulosis ',
    'Cholecystitis',
    'Sarcoma',
    'Fibroids',
    'Chronic fatigue syndrome',
    'Fibromyalgia',
    'Systemic lupus erythamatosis ',
    'Bechets ',
    'Scleroderma',
    'Gout',
    'Pleural effusion',
    'Ascites',
    'Dislocation',
    )
    return random.choice(conditions)

def medications():
    meds = ('Paracetamol',
    'Ibuprofen',
    'Co-codamol',
    'Codeine',
    'Tramadol',
    'Morphine',
    'Diclofenac',
    'Asprin',
    'Naproxen',
    'Dihydrocodeine',
    'Oxycodone',
    'Nefopam',
    'Gabapentin',
    'Fentanyl',
    'Ketamine',
    'Bisoprolol',
    'Atenolol',
    'Digoxin',
    'Amiodarone',
    'Adenosine',
    'Diltiazem',
    'Amoxicillin',
    'Flucloxacillin',
    'Meropenem',
    'Vancomycin',
    'Gentamycin',
    'Clarithromycin',
    'Co-amoxiclav',
    'Doxycycline',
    'Ceftazidime',
    'Ciprofloxacin',
    'Levofloxacin',
    'Cephalexin',
    'Cefuroxime',
    'Clindamycin',
    'Trimethoprim',
    'Nitrofurantoin',
    'Warfarin',
    'Rivaroxaban',
    'Apixaban',
    'Enoxaparin',
    'Sodium valproate',
    'Phenytoin',
    'Levetiracetam',
    'Gabapentin',
    'Clonazepam',
    'Diazapam',
    'Lorazepam',
    'Carbamazepine',
    'Citalopram',
    'Fluoxetine',
    'Amitriptyline',
    'Sertraline',
    'Venlafaxine',
    'Mirtazapine',
    'Trazodone',
    'Ramipril',
    'Doxazosin',
    'Candesartan',
    'Losartan',
    'Lisinopril',
    'Atenolol',
    'Bisoprolol',
    'Amlodipine',
    'Diltiazem',
    'Nifedipine',
    'Metformin',
    'Insulin',
    'Gliclazide',
    'Salbutamol',
    'Ipratropium',
    'Tiotropium',
    'Theophylline',
    'Furosemide',
    'Bumetanide',
    'Spironolactone',
    'Bendroflumethiazide',
    'Indapamide',
    'Amiloride')
    return random.choice(meds)

def clinicletter():
    stylesheet=getSampleStyleSheet()
    normalStyle = stylesheet['Normal']

    ptext = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Integer ultrices neque mattis vestibulum imperdiet. Nulla sit amet tincidunt quam. Pellentesque malesuada tristique sollicitudin. Pellentesque eu augue finibus, posuere sem auctor, ultricies nibh. Curabitur molestie lectus pellentesque, malesuada augue nec, maximus lorem. Maecenas viverra velit mauris, id rhoncus libero porta sit amet. Curabitur molestie gravida bibendum. Nunc posuere magna pellentesque felis aliquam, sit amet vestibulum magna pulvinar. Ut vulputate vulputate urna, ac porttitor ex vehicula elementum"

    p = Paragraph(ptext, normalStyle)
    filename = newfilename()
    c = Canvas('%s.pdf' % filename)

    c.drawImage('NHSRGB.jpg', 425, 750, width=125, height=50)

    c.drawString(100,800, "Clinic Date")

    c.drawString(100,750, "This Hospital")
    c.drawString(100,735, "Somewhere")
    c.drawString(100,720, "NW4 FTP")

    #random names
    first_names=('John','Andy','Joe', 'Charles', 'Donald', 'Terrance')
    last_names=('Johnson','Smith','Williams', 'Sanchez', 'Holt', 'Selby')
    full_name = random.choice(first_names) + " " + random.choice(last_names)

    #random date
    year = random.randint(1930, 2000)
    month = random.randint(1, 12)
    day = random.randint(1, 28)
    birth_date = date(year, month, day)

    nhsno = random.randint(4440001111, 7001110000)

    something = str(birth_date)
    somethings = str(nhsno)
    c.drawString(100, 650, full_name +  ", " + something +  ", NHS number:" +  somethings)
    c.drawString(100, 600, "Dear patient, ")

    c.drawString(100, 550, "Diagnoses:")

    x = 200
    y = 550

    numconditions = random.randint(1,5)


    for num in range(numconditions):
        condition = randcondtion()
        c.drawString(x, y, condition)
        y = y - 15

    y = y-20
    c.drawString(100,y, "Medications:")
    nummedications = random.randint(1,10)
    for num in range(nummedications):
        medication = medications()
        c.drawString(x, y, medication)
        y = y - 15

    y = y-100

    p.wrap(450,400)
    p.drawOn(c, 100, y)

    y = y-100

    ptext = "Duis ut vulputate elit. Nullam sodales dui vestibulum porta eleifend. Mauris a elementum nunc, quis volutpat urna. Vivamus auctor ex id eleifend pellentesque. Donec congue leo lacus, sed iaculis velit fringilla vel. Ut vehicula turpis vel tincidunt vulputate. Nullam aliquam enim sit amet fringilla tincidunt. Cras eu mi massa. In pulvinar tempor nulla in cursus. Aenean a elit eget enim bibendum pellentesque. Nulla at felis sagittis, consequat orci sed, cursus sapien."

    p = Paragraph(ptext, normalStyle)
    p.wrap(450,400)
    p.drawOn(c, 100, y)
    c.save()

clinicletter()
