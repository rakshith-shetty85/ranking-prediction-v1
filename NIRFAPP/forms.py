from django import forms

class Students(forms.Form):
    MStud=forms.IntegerField()
    FStud=forms.IntegerField()
    TStud=forms.IntegerField()
    WINState=forms.IntegerField()
    OOFState=forms.IntegerField()
    OOFCountry=forms.IntegerField()
    EBC=forms.IntegerField()
    SChalenged=forms.IntegerField()
    RemSandC=forms.IntegerField()
    RemInst=forms.IntegerField()
    RemPrev=forms.IntegerField()
    NoRem=forms.IntegerField()
    MStud1 = forms.IntegerField()
    FStud1 = forms.IntegerField()
    TStud1 = forms.IntegerField()
    WINState1 = forms.IntegerField()
    OOFState1 = forms.IntegerField()
    OOFCountry1 = forms.IntegerField()
    EBC1 = forms.IntegerField()
    SChalenged1 = forms.IntegerField()
    RemSandC1 = forms.IntegerField()
    RemInst1 = forms.IntegerField()
    RemPrev1 = forms.IntegerField()
    NoRem1 = forms.IntegerField()
    MStud2 = forms.IntegerField()
    FStud2 = forms.IntegerField()
    TStud2 = forms.IntegerField()
    WINState2 = forms.IntegerField()
    OOFState2 = forms.IntegerField()
    OOFCountry2 = forms.IntegerField()
    EBC2 = forms.IntegerField()
    SChalenged2 = forms.IntegerField()
    RemSandC2 = forms.IntegerField()
    RemInst2 = forms.IntegerField()
    RemPrev2 = forms.IntegerField()
    NoRem2 = forms.IntegerField()
    Intake11 = forms.IntegerField()
    Intake12 = forms.IntegerField()
    Intake13 = forms.IntegerField()
    Intake14 = forms.IntegerField()
    Intake21 = forms.IntegerField()
    Intake22 = forms.IntegerField()
    Intake23 = forms.IntegerField()
    Intake24 = forms.IntegerField()
    Intake31 = forms.IntegerField()
    Intake32 = forms.IntegerField()
    Intake33 = forms.IntegerField()
    Intake34 = forms.IntegerField()
    Intake41 = forms.IntegerField()
    Intake42 = forms.IntegerField()
    Intake43 = forms.IntegerField()
    Intake44 = forms.IntegerField()
    FstIntake11=forms.IntegerField()
    FstAdmit11=forms.IntegerField()
    Lateral11=forms.IntegerField()
    GMTime11=forms.IntegerField()
    Placed11=forms.IntegerField()
    MedianSal11=forms.IntegerField()
    SelectedHigh11=forms.IntegerField()
    FstIntake12 = forms.IntegerField()
    FstAdmit12 = forms.IntegerField()
    Lateral12 = forms.IntegerField()
    GMTime12 = forms.IntegerField()
    Placed12 = forms.IntegerField()
    MedianSal12 = forms.IntegerField()
    SelectedHigh12 = forms.IntegerField()
    FstIntake13 = forms.IntegerField()
    FstAdmit13 = forms.IntegerField()
    Lateral13 = forms.IntegerField()
    GMTime13 = forms.IntegerField()
    Placed13 = forms.IntegerField()
    MedianSal13 = forms.IntegerField()
    SelectedHigh13 = forms.IntegerField()
    FstIntake21 = forms.IntegerField()
    FstAdmit21 = forms.IntegerField()
    Lateral21 = forms.IntegerField()
    GMTime21 = forms.IntegerField()
    Placed21 = forms.IntegerField()
    MedianSal21 = forms.IntegerField()
    SelectedHigh21 = forms.IntegerField()
    FstIntake22 = forms.IntegerField()
    FstAdmit22 = forms.IntegerField()
    Lateral22 = forms.IntegerField()
    GMTime22 = forms.IntegerField()
    Placed22 = forms.IntegerField()
    MedianSal22 = forms.IntegerField()
    SelectedHigh22 = forms.IntegerField()
    FstIntake23 = forms.IntegerField()
    FstAdmit23 = forms.IntegerField()
    Lateral23 = forms.IntegerField()
    GMTime23 = forms.IntegerField()
    Placed23 = forms.IntegerField()
    MedianSal23 = forms.IntegerField()
    SelectedHigh23 = forms.IntegerField()
    FstIntake31 = forms.IntegerField()
    FstAdmit31 = forms.IntegerField()
    GMTime31 = forms.IntegerField()
    Placed31 = forms.IntegerField()
    MedianSal31 = forms.IntegerField()
    SelectedHigh31 = forms.IntegerField()
    FstIntake32 = forms.IntegerField()
    FstAdmit32 = forms.IntegerField()
    GMTime32 = forms.IntegerField()
    Placed32 = forms.IntegerField()
    MedianSal32 = forms.IntegerField()
    SelectedHigh32 = forms.IntegerField()
    FstIntake33 = forms.IntegerField()
    FstAdmit33 = forms.IntegerField()
    GMTime33 = forms.IntegerField()
    Placed33 = forms.IntegerField()
    MedianSal33 = forms.IntegerField()
    SelectedHigh33 = forms.IntegerField()
    FstIntake41 = forms.IntegerField()
    FstAdmit41 = forms.IntegerField()
    Lateral41 = forms.IntegerField()
    GMTime41 = forms.IntegerField()
    Placed41 = forms.IntegerField()
    MedianSal41 = forms.IntegerField()
    SelectedHigh41 = forms.IntegerField()
    FstIntake42 = forms.IntegerField()
    FstAdmit42 = forms.IntegerField()
    Lateral42 = forms.IntegerField()
    GMTime42 = forms.IntegerField()
    Placed42 = forms.IntegerField()
    MedianSal42 = forms.IntegerField()
    SelectedHigh42 = forms.IntegerField()
    FstIntake43 = forms.IntegerField()
    FstAdmit43 = forms.IntegerField()
    Lateral43 = forms.IntegerField()
    GMTime43 = forms.IntegerField()
    Placed43 = forms.IntegerField()
    MedianSal43 = forms.IntegerField()
    SelectedHigh43 = forms.IntegerField()
    FtimePHD=forms.IntegerField()
    PtimePHD=forms.IntegerField()
    FtimePHD1=forms.IntegerField()
    FtimePHD2=forms.IntegerField()
    FtimePHD3=forms.IntegerField()
    PtimePHD1=forms.IntegerField()
    PtimePHD2=forms.IntegerField()
    PtimePHD3=forms.IntegerField()
    PCS1=forms.CharField(max_length=200)
    PCS2=forms.CharField(max_length=200)
    PCS3=forms.CharField(max_length=200)

class SecondaryForm(forms.Form):
    TLR=forms.FloatField()
    RP=forms.FloatField()
    GO=forms.FloatField()
    OI=forms.FloatField()
    PR=forms.FloatField()

class SecondaryForm1(forms.Form):
    TLR=forms.FloatField()
    RP=forms.FloatField()
    GO=forms.FloatField()
    OI=forms.FloatField()
    PR=forms.FloatField()