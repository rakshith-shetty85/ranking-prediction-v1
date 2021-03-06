# Generated by Django 3.2.3 on 2021-05-20 06:24

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Secondarydata',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('TLR', models.IntegerField()),
                ('RP', models.IntegerField()),
                ('GO', models.IntegerField()),
                ('OI', models.IntegerField()),
                ('PR', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Secondarydata11',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('SS', models.IntegerField()),
                ('FSR', models.IntegerField()),
                ('FQE', models.IntegerField()),
                ('FRU', models.IntegerField()),
                ('PU', models.IntegerField()),
                ('QP', models.IntegerField()),
                ('IPR', models.IntegerField()),
                ('FPPP', models.IntegerField()),
                ('GPH', models.IntegerField()),
                ('GUE', models.IntegerField()),
                ('GMS', models.IntegerField()),
                ('GPHD', models.IntegerField()),
                ('RD', models.IntegerField()),
                ('WD', models.IntegerField()),
                ('ESCS', models.IntegerField()),
                ('PCS', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='UGStuClass',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('MStud', models.IntegerField()),
                ('FStud', models.IntegerField()),
                ('TStud', models.IntegerField()),
                ('WINState', models.IntegerField()),
                ('OOFState', models.IntegerField()),
                ('OOFCountry', models.IntegerField()),
                ('EBC', models.IntegerField()),
                ('SChalenged', models.IntegerField()),
                ('RemSandC', models.IntegerField()),
                ('RemInst', models.IntegerField()),
                ('RemPrev', models.IntegerField()),
                ('NoRem', models.IntegerField()),
                ('MStud1', models.IntegerField()),
                ('FStud1', models.IntegerField()),
                ('TStud1', models.IntegerField()),
                ('WINState1', models.IntegerField()),
                ('OOFState1', models.IntegerField()),
                ('OOFCountry1', models.IntegerField()),
                ('EBC1', models.IntegerField()),
                ('SChalenged1', models.IntegerField()),
                ('RemSandC1', models.IntegerField()),
                ('RemInst1', models.IntegerField()),
                ('RemPrev1', models.IntegerField()),
                ('NoRem1', models.IntegerField()),
                ('MStud2', models.IntegerField()),
                ('FStud2', models.IntegerField()),
                ('TStud2', models.IntegerField()),
                ('WINState2', models.IntegerField()),
                ('OOFState2', models.IntegerField()),
                ('OOFCountry2', models.IntegerField()),
                ('EBC2', models.IntegerField()),
                ('SChalenged2', models.IntegerField()),
                ('RemSandC2', models.IntegerField()),
                ('RemInst2', models.IntegerField()),
                ('RemPrev2', models.IntegerField()),
                ('NoRem2', models.IntegerField()),
                ('Intake11', models.IntegerField()),
                ('Intake12', models.IntegerField()),
                ('Intake13', models.IntegerField()),
                ('Intake14', models.IntegerField()),
                ('Intake21', models.IntegerField()),
                ('Intake22', models.IntegerField()),
                ('Intake23', models.IntegerField()),
                ('Intake24', models.IntegerField()),
                ('Intake31', models.IntegerField()),
                ('Intake32', models.IntegerField()),
                ('Intake33', models.IntegerField()),
                ('Intake34', models.IntegerField()),
                ('Intake41', models.IntegerField()),
                ('Intake42', models.IntegerField()),
                ('Intake43', models.IntegerField()),
                ('Intake44', models.IntegerField()),
                ('FstIntake11', models.IntegerField()),
                ('FstAdmit11', models.IntegerField()),
                ('Lateral11', models.IntegerField()),
                ('GMTime11', models.IntegerField()),
                ('Placed11', models.IntegerField()),
                ('MedianSal11', models.IntegerField()),
                ('SelectedHigh11', models.IntegerField()),
                ('FstIntake12', models.IntegerField()),
                ('FstAdmit12', models.IntegerField()),
                ('Lateral12', models.IntegerField()),
                ('GMTime12', models.IntegerField()),
                ('Placed12', models.IntegerField()),
                ('MedianSal12', models.IntegerField()),
                ('SelectedHigh12', models.IntegerField()),
                ('FstIntake13', models.IntegerField()),
                ('FstAdmit13', models.IntegerField()),
                ('Lateral13', models.IntegerField()),
                ('GMTime13', models.IntegerField()),
                ('Placed13', models.IntegerField()),
                ('MedianSal13', models.IntegerField()),
                ('SelectedHigh13', models.IntegerField()),
                ('FstIntake21', models.IntegerField()),
                ('FstAdmit21', models.IntegerField()),
                ('Lateral21', models.IntegerField()),
                ('GMTime21', models.IntegerField()),
                ('Placed21', models.IntegerField()),
                ('MedianSal21', models.IntegerField()),
                ('SelectedHigh21', models.IntegerField()),
                ('FstIntake22', models.IntegerField()),
                ('FstAdmit22', models.IntegerField()),
                ('Lateral22', models.IntegerField()),
                ('GMTime22', models.IntegerField()),
                ('Placed22', models.IntegerField()),
                ('MedianSal22', models.IntegerField()),
                ('SelectedHigh22', models.IntegerField()),
                ('FstIntake23', models.IntegerField()),
                ('FstAdmit23', models.IntegerField()),
                ('Lateral23', models.IntegerField()),
                ('GMTime23', models.IntegerField()),
                ('Placed23', models.IntegerField()),
                ('MedianSal23', models.IntegerField()),
                ('SelectedHigh23', models.IntegerField()),
                ('FstIntake31', models.IntegerField()),
                ('FstAdmit31', models.IntegerField()),
                ('GMTime31', models.IntegerField()),
                ('Placed31', models.IntegerField()),
                ('MedianSal31', models.IntegerField()),
                ('SelectedHigh31', models.IntegerField()),
                ('FstIntake32', models.IntegerField()),
                ('FstAdmit32', models.IntegerField()),
                ('GMTime32', models.IntegerField()),
                ('Placed32', models.IntegerField()),
                ('MedianSal32', models.IntegerField()),
                ('SelectedHigh32', models.IntegerField()),
                ('FstIntake33', models.IntegerField()),
                ('FstAdmit33', models.IntegerField()),
                ('GMTime33', models.IntegerField()),
                ('Placed33', models.IntegerField()),
                ('MedianSal33', models.IntegerField()),
                ('SelectedHigh33', models.IntegerField()),
                ('FstIntake41', models.IntegerField()),
                ('FstAdmit41', models.IntegerField()),
                ('Lateral41', models.IntegerField()),
                ('GMTime41', models.IntegerField()),
                ('Placed41', models.IntegerField()),
                ('MedianSal41', models.IntegerField()),
                ('SelectedHigh41', models.IntegerField()),
                ('FstIntake42', models.IntegerField()),
                ('FstAdmit42', models.IntegerField()),
                ('Lateral42', models.IntegerField()),
                ('GMTime42', models.IntegerField()),
                ('Placed42', models.IntegerField()),
                ('MedianSal42', models.IntegerField()),
                ('SelectedHigh42', models.IntegerField()),
                ('FstIntake43', models.IntegerField()),
                ('FstAdmit43', models.IntegerField()),
                ('Lateral43', models.IntegerField()),
                ('GMTime43', models.IntegerField()),
                ('Placed43', models.IntegerField()),
                ('MedianSal43', models.IntegerField()),
                ('SelectedHigh43', models.IntegerField()),
                ('FtimePHD', models.IntegerField()),
                ('PtimePHD', models.IntegerField()),
                ('FtimePHD1', models.IntegerField()),
                ('FtimePHD2', models.IntegerField()),
                ('FtimePHD3', models.IntegerField()),
                ('PtimePHD1', models.IntegerField()),
                ('PtimePHD2', models.IntegerField()),
                ('PtimePHD3', models.IntegerField()),
                ('PCS1', models.CharField(max_length=200)),
                ('PCS2', models.CharField(max_length=200)),
                ('PCS3', models.CharField(max_length=200)),
            ],
        ),
    ]
