**EHF attachment xml to pdf converter**

I programmed this code because many invoice software when not send out correct, they store the pdf as xml.

This is for converting it back to PDF so we can read what invoice is is , and then can be resend or imported to main software.


**Reference**

[EHF Overview](http://connect.demo.ibxplatform.com/IBX%20Connect%20-%20EHF.html)

**EHF**
EHF is an anagram of the Norwegian expression << **E** lektronisk **h** andels **f** ormat>> (Electronic Commerce Format).

EHF is the standard format for electronic invoices and credit notes for the public sector of Norway. It is based on the XML format UBL 2.0 and on business processes or profiles defined by the European wide [CEN/BII](http://www.cen.eu/cwa/bii/specs/ "CEN/ISSS Business Interoperability Interfaces for Public procurement in Europe (CENBII)") workshop. Invoices in [EHF format](http://www.anskaffelser.no/e-handel/dokumenter/ehandel.no-formatet "Elektronisk handelsformat (EHF) - official homepage") meet the requirements of the Norwegian Accounting Act. The EHF standard is maintained by [DIFI](http://www.difi.no/ "DIFI - official homepage"), the Agency for Public Management and eGovernment in Norway. Since the IBX Connect platform is an official PEPPOL AccessPoint EHF Invoices, CreditNotes and Reminders can be exchanged via the PEPPOL infrastructure as well as via the standard IBX Connect interfaces: via HTTPs and FTPs/SFTP with or without SOAP envelope.  
During autumn 2013 an implementation guide also for orders and orderresponses according to EHF and UBL 2.1 standards will be released officially. Examples of purchase orders and orderresponses fulfilling the EHF requirements can be found on this website.

**How to**
simply drag the xml into convert_attachment.py

or from command prompt

`convert_attachment.py file.xml`

**Test files**

**EHF Invoice examples**

* [EHF Invoice example with standard elements and SOAP 1.2 envelope including an embedded attachment](http://connect.demo.ibxplatform.com/xml/SOAP12_EHF%20Invoice%20example%20simple%20with%20BLOB%20attachment.xml "EHF Invoice example with standard elements and SOAP 1.2 envelope including an embedded attachment")

**EHF Invoice examples**

[EHF CreditNote example with standard elements and SOAP 1.2 envelope including an embedded attachment](http://connect.demo.ibxplatform.com/xml/SOAP12_EHF%20CreditNote%20example%20simple%20with%20BLOB%20attachment.xml "EHF CreditNote example with standard elements and SOAP 1.2 envelope including an embedded attachment")

**Screenshot**

after conversion you should have a copy of the invoice.

![invoice](https://cloud.githubusercontent.com/assets/3592375/23343757/c501b452-fc70-11e6-9a29-fcf8d54b24c1.png)
