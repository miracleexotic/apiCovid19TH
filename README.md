# COVID19-Thailand API

## Announcement
**Note**: api นี้ใช้สำหรับติดตามรายละเอียดและข้อมูลของ Covid-19 ในประเทศไทยเท่านั้น
ตัว api ทำงานช้าไม่เหมาะต่อการใช้งาน พัฒนาขึ้นมาเพื่อศึกษาเรียนรู้และใช้งานในบางกรณี

### Information
**Note**: json data
Web scraping from https://ddc.moph.go.th/viralpneumonia/eng/index.php
- DayfromWeb
: วันที่อัพเดตจากเว็บ
- Deaths
: เสียชีวิต
- New
: case ใหม่
- Serious
- TimefromWeb
: เวลาที่อัพเดตจากเว็บ
- currentTime
: เวลา ณ ปัจจุบัน ขณะเรียกใช้ api
- total
: ยอดรวม

### Used
    GET method : https://api-covid19-th.herokuapp.com/api/covid19-TH

