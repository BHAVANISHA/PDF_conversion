from fpdf import FPDF

details = {
    "first_name": "Donna",
    "last_name": "Johnson",
    "date_of_birth": "N/A",
    "position": "NOC Systems Desktop Specialist",
    "description": "To secure a position that will utilize my computer skills and management experience offering opportunity for professional growth in a dynamic environment.",
    "email_id": "Donna62John@yahoo.com",
    "mobile_number": "470-213-4277",
    "location": "Duluth, GA 30096",
    "years_of_experience": "N/A",
    "current_position": "NOC Systems Desktop Specialist",
    "current_company": "Milner Technology Services",
    "current_company_domain": "N/A",
    "current_company_business": "N/A",
    "previous_company": "IBM (Contracting through Artech)",
    "work_authorization": "N/A",
    "clearance": "N/A",
    "address": "1060 Court Drive Apt. S, Duluth, GA 30096",
    "disability": "N/A",
    "primary_skills": "A+ Certified Information Technology professional, MS Windows support, MS Servers support, Application support, LAN Administration, troubleshooting, repairing Dell, IBM/Lenova and HP desktops, laptops, printers, switches and peripherals, TCPIP and DNS errors, VPN setup and support",
    "social_media_id": "N/A",
    "patents_info": "N/A",
    "previous_domain_worked_history": "N/A",
    "linkedin_url": "N/A",
    "education": "[{\"school_or_college\":\"Brevard County Community College\",\"course_name\":\"Computer Repair Technology\",\"years\":\"N/A\"}]",
    "work_experience": "["
                       "{\"position\":\"NOC Systems Desktop Specialist\","
                       "\"years\":\"4/14-8/27/19\","
                       "\"company\":\"Milner Technology Services\",\"domain\":\"N/A\""
                       "},"
                       "{\"position\":\"IT Desktop Support Specialist\",\"years\":\"5/12-12/20/13\",\"company\":\"IBM (Contracting through Artech)\",\"domain\":\"N/A\"},{\"position\":\"IT Desktop Support Specialist\",\"years\":\"9/11-12/11\",\"company\":\"Pima County (Yoh | A Day & Zimmermann Company)\",\"domain\":\"N/A\"},{\"position\":\"IT Desktop Support Specialist\",\"years\":\"5/11-7/11\",\"company\":\"Sun Trust Bank (Contracted through APEX)\",\"domain\":\"N/A\"},{\"position\":\"Helpdesk Coordinator\",\"years\":\"2/11-4/11\",\"company\":\"CDC (Contracted with TekSystems)\",\"domain\":\"N/A\"},{\"position\":\"IT Desktop Support Specialist\",\"years\":\"6/10-7/10\",\"company\":\"John Deere (short term contract through United Global)\",\"domain\":\"N/A\"},{\"position\":\"Desktop Support Specialist\",\"years\":\"2/09-10/09\",\"company\":\"Forsyth County School Board- Atlanta GA (contracting through Think Resources)\",\"domain\":\"N/A\"},{\"position\":\"IT Desktop Support Specialist\",\"years\":\"6/2005-2/2009\",\"company\":\"FUNDtech Corporation- Atlanta GA (contracted through Think Resources 7/05-2/06)\",\"domain\":\"N/A\"},{\"position\":\"Corporate Support Helpdesk Center Specialist\",\"years\":\"10/03-7/04\",\"company\":\"Blue Cross Blue Shield of Alabama- Birmingham, AL (Contracted through Comforce for six months)\",\"domain\":\"N/A\"},{\"position\":\"Computer Repair Technician\",\"years\":\"10/02-3/03\",\"company\":\"CompUSA- Birmingham, AL\",\"domain\":\"N/A\"},{\"position\":\"Distributed Computer Support Specialist\",\"years\":\"4/98-3/2002\",\"company\":\"Brevard County Clerk of Courts- Titusville, FL\",\"domain\":\"N/A\"},{\"position\":\"Information Technology Technician\",\"years\":\"2/96-4/98\",\"company\":\"Central Data Computer Center- Titusville, FL\",\"domain\":\"N/A\"},{\"position\":\"Lead Technician\",\"years\":\"4/85-7/95\",\"company\":\"McDonnell-Douglas Inc- Titusville FL\",\"domain\":\"N/A\"}]",
    "interests": "'N/A'",
    "speaking_languages": "'N/A'",
    "skills": "'A+ Certified Information Technology professional', ' MS Windows support', ' MS Servers support', ' Application support', ' LAN Administration', ' troubleshooting', ' repairing Dell', ' IBM/Lenova and HP desktops', ' laptops', ' printers', ' switches and peripherals', ' TCPIP and DNS errors', ' VPN setup and support'",
    "projects_list": "'N/A'",
    "achievements": "'N/A'",
    "extra_activities": "'N/A'",
    "certificates": "'Microsoft A+ Certified', 'HP, Compaq, Dell, IBM warranty certifications'",
    "city": "Duluth",
    "state": "GA",
    "job_title": "NOC Systems Desktop Specialist",
    "resume_html_tag": "undefined",
    "source": "extension"
}


class PDF( FPDF ):
    def header(self):
        if self.page_no() == 1:
            self.set_font( 'Arial', 'B', 12 )
            self.cell( 0, 20, 'Candidate Resume', 0, 1, 'C' )

    def footer(self):
        self.set_y( -15 )
        self.set_font( 'Arial', 'I', 8 )
        self.cell( 0, 10, 'Page %s' % self.page_no(), 0, 0, 'C' )

    def add_details(self, details):
        self.set_font( 'Arial', 'B', 12 )
        full_name = details['first_name'] + ' ' + details['last_name']
        entire_name = full_name.encode( 'latin-1', 'replace' ).decode( 'latin-1' )
        self.cell( 0, 8, entire_name, ln=True )
        self.set_font( 'Arial', '', 10 )
        position = details['position'].encode( 'latin-1', 'replace' ).decode( 'latin-1' )
        self.cell( 0, 6, 'Job title :' + " " + position, ln=True )
        location = details['location'].encode( 'latin-1', 'replace' ).decode( 'latin-1' )
        self.cell( 0, 6, "location :" + " " + location, ln=True )
        email_id = details['email_id'].encode( 'latin-1', 'replace' ).decode( 'latin-1' )
        self.cell( 0, 6, 'Email :' + " " + email_id, ln=True )
        mobile_number = details['mobile_number'].encode( 'latin-1', 'replace' ).decode( 'latin-1' )
        self.cell( 0, 6, "Mobile :" + " " + mobile_number, ln=True )
        d_o_b = details['date_of_birth'].encode( 'latin-1', 'replace' ).decode( 'latin-1' )
        self.cell( 0, 6, "Date of Birth :" + " " + d_o_b, ln=True )

        self.ln( 3 )
        self.set_font( 'Arial', 'BU', 12 )
        self.cell( 0, 10, 'Summary', ln=True )
        self.set_font( 'Arial', '', 10 )
        description = details['description'].encode( 'latin-1', 'replace' ).decode( 'latin-1' )
        self.multi_cell( 0, 5, description )

        self.ln( 3 )
        self.set_font( 'Arial', 'BU', 12 )
        self.cell( 0, 10, 'Education', ln=True )
        self.set_font( 'Arial', '', 10 )
        if type( details['education'] ) == str:
            education_list = eval( details['education'] )
            for education in education_list:
                school_or_college = education['school_or_college'].encode( 'latin-1', 'replace' ).decode( 'latin-1' )
                self.cell( 0, 6, "School/College: " + school_or_college, ln=True )
                course_name = education['course_name'].encode( 'latin-1', 'replace' ).decode( 'latin-1' )
                self.cell( 0, 6, "Course Name: " + course_name, ln=True )
                years = education['years'].encode( 'latin-1', 'replace' ).decode( 'latin-1' )
                self.cell( 0, 6, "Years: " + years, ln=True )

        self.ln( 3 )
        self.set_font( 'Arial', 'BU', 12 )
        self.cell( 0, 10, 'Skills', ln=True )
        self.set_font( 'Arial', '', 10 )
        if type( details['skills'] ) == str:
            skills_list = eval( details['skills'] )
            for skills in skills_list:
                skills = skills.encode( 'latin-1', 'replace' ).decode( 'latin-1' )
                self.cell( 0, 6, skills, ln=True )

        self.ln( 3 )
        self.set_font( 'Arial', 'BU', 12 )
        self.cell( 0, 10, 'Work Experience', ln=True )
        self.set_font( 'Arial', '', 10 )
        if type( details['education'] ) == str:
            work_experience = eval( details['work_experience'] )
            for experience in work_experience:
                self.set_font( 'Arial', 'BU', 10 )
                position = experience['position'].encode( 'latin-1', 'replace' ).decode( 'latin-1' )
                self.cell( 0, 6, "Position: " + position, ln=True )
                self.set_font( 'Arial', '', 10 )
                company = experience['company'].encode( 'latin-1', 'replace' ).decode( 'latin-1' )
                self.cell( 0, 6, "Company: " + company, ln=True )
                years = experience['years'].encode( 'latin-1', 'replace' ).decode( 'latin-1' )
                self.cell( 0, 6, "Years: " + years, ln=True )
                domain = experience['domain'].encode( 'latin-1', 'replace' ).decode( 'latin-1' )
                self.cell( 0, 6, "Domain: " + domain, ln=True )
                self.ln( 4 )

        self.ln( 3 )
        self.set_font( 'Arial', 'BU', 12 )
        self.cell( 0, 10, 'Interests', ln=True )
        self.set_font( 'Arial', '', 10 )
        interests = details['interests'].replace( "'", '' ).encode( 'latin-1', 'replace' ).decode( 'latin-1' )
        self.cell( 0, 6, interests, ln=True )
        self.set_font( 'Arial', 'BU', 12 )
        self.cell( 0, 10, 'Speaking Languages', ln=True )
        self.set_font( 'Arial', '', 10 )
        speaking_languages = details['speaking_languages'].replace( "'", '' ).encode( 'latin-1', 'replace' ).decode(
            'latin-1' )
        self.cell( 0, 6, speaking_languages, ln=True )

        self.ln( 3 )
        self.set_font( 'Arial', 'BU', 12 )
        certificates = details['certificates'].encode( 'latin-1', 'replace' ).decode( 'latin-1' )
        self.cell( 0, 10, 'Certificates', ln=True )
        self.set_font( 'Arial', '', 10 )
        for certificate in details['certificates'].split(","):
            self.multi_cell( 0, 6, certificate )

        self.ln( 3 )
        self.set_font( 'Arial', 'BU', 12 )
        self.cell( 0, 10, 'Achievements', ln=True )
        self.set_font( 'Arial', '', 10 )
        for achievement in details['achievements'].split( "," ):
            achievement = achievement.replace( "'", '' ).encode( 'latin-1', 'replace' ).decode( 'latin-1' )
            self.multi_cell( 0, 6, achievement.replace( '’', '' ) )

        self.set_font( 'Arial', 'BU', 12 )
        self.cell( 0, 10, 'Projects List', ln=True )
        self.set_font( 'Arial', '', 10 )
        for project in details['projects_list'].split( "," ):
            projects_list = project.replace( "'", '' ).encode( 'latin-1', 'replace' ).decode( 'latin-1' )
            self.multi_cell( 0, 6, projects_list )

        self.ln( 3 )
        self.set_font( 'Arial', 'BU', 12 )
        self.cell( 0, 6, 'Years Of Experience:', ln=True )
        self.set_font( 'Arial', '', 10 )
        years_of_experience = details['years_of_experience'].encode( 'latin-1', 'replace' ).decode( 'latin-1' )
        self.cell( 0, 6, years_of_experience, ln=True )

        self.ln( 3 )
        self.set_font( 'Arial', 'BU', 12 )
        self.cell( 0, 10, 'Current_position:', ln=True )
        self.set_font( 'Arial', '', 10 )
        current_position = details['current_position'].encode( 'latin-1', 'replace' ).decode( 'latin-1' )
        self.multi_cell( 0, 5, current_position )

        self.set_y( self.get_y() - 14 )
        self.set_x( self.w - 90 )
        self.set_font( 'Arial', 'BU', 12 )
        self.cell( 0, 10, 'Current_company:', ln=True )
        self.set_font( 'Arial', '', 10 )
        self.set_y( self.get_y() - 0 )
        self.set_x( self.w - 90 )
        current_company = details['current_company'].encode( 'latin-1', 'replace' ).decode( 'latin-1' )
        self.multi_cell( 0, 5, current_company )

        self.ln( 3 )
        self.set_font( 'Arial', 'BU', 12 )
        self.cell( 0, 10, 'Current_company_domain:', ln=True )
        self.set_font( 'Arial', '', 10 )
        current_company_domain = details['current_company_domain'].encode( 'latin-1', 'replace' ).decode( 'latin-1' )
        self.multi_cell( 0, 5, current_company_domain )

        self.set_y( self.get_y() - 14 )
        self.set_x( self.w - 90 )
        self.set_font( 'Arial', 'BU', 12 )
        self.cell( 0, 10, 'Current_company_business:', ln=True )
        self.set_font( 'Arial', '', 10 )
        self.set_y( self.get_y() - 0 )
        self.set_x( self.w - 90 )
        current_company_business = details['current_company_business'].encode( 'latin-1', 'replace' ).decode('latin-1' )
        self.multi_cell( 0, 5, current_company_business )

        self.ln( 3 )
        self.set_font( 'Arial', 'BU', 12 )
        self.cell( 0, 10, 'Previous_company:', ln=True )
        self.set_font( 'Arial', '', 10 )
        previous_company = details['previous_company'].encode( 'latin-1', 'replace' ).decode( 'latin-1' )
        self.multi_cell( 0, 5, previous_company )

        self.set_y( self.get_y() - 14 )
        self.set_x( self.w - 90 )
        self.set_font( 'Arial', 'BU', 12 )
        self.cell( 0, 10, 'Previous_domain_worked_history:', ln=True )
        self.set_font( 'Arial', '', 10 )
        self.set_y( self.get_y() - 0 )
        self.set_x( self.w - 90 )
        previous_domain_worked_history = details['previous_domain_worked_history'].encode( 'latin-1','replace' ).decode('latin-1' )
        self.multi_cell( 0, 5, previous_domain_worked_history )

        self.ln( 3 )
        self.set_font( 'Arial', 'BU', 12 )
        self.cell( 0, 10, 'Work_authorization:', ln=True )
        self.set_font( 'Arial', '', 10 )
        work_authorization = details['work_authorization'].encode( 'latin-1', 'replace' ).decode( 'latin-1' )
        self.multi_cell( 0, 5, work_authorization )

        self.set_y( self.get_y() - 14 )
        self.set_x( self.w - 90 )
        self.set_font( 'Arial', 'BU', 12 )
        self.cell( 0, 10, 'Clearance:', ln=True )
        self.set_font( 'Arial', '', 10 )
        self.set_y( self.get_y() - 0 )
        self.set_x( self.w - 90 )
        clearance = details['clearance'].encode( 'latin-1', 'replace' ).decode( 'latin-1' )
        self.multi_cell( 0, 5, clearance )

        self.ln( 3 )
        self.set_font( 'Arial', 'BU', 12 )
        self.cell( 0, 10, 'Address', ln=True )
        self.set_font( 'Arial', '', 10 )
        address = details['address'].encode( 'latin-1', 'replace' ).decode( 'latin-1' )
        self.multi_cell( 0, 6, address )

        self.ln( 3 )
        self.set_font( 'Arial', 'BU', 12 )
        self.cell( 0, 10, 'Disability:', ln=True )
        self.set_font( 'Arial', '', 10 )
        disability = details['disability'].encode( 'latin-1', 'replace' ).decode( 'latin-1' )
        self.multi_cell( 0, 5, disability )

        self.set_y( self.get_y() - 14 )
        self.set_x( self.w - 90 )
        self.set_font( 'Arial', 'BU', 12 )
        self.cell( 0, 10, 'Patents_info:', ln=True )
        self.set_font( 'Arial', '', 10 )
        self.set_y( self.get_y() - 0 )
        self.set_x( self.w - 90 )
        patents_info = details['patents_info'].encode( 'latin-1', 'replace' ).decode( 'latin-1' )
        self.multi_cell( 0, 5, patents_info )

        self.ln( 3 )
        self.set_font( 'Arial', 'BU', 12 )
        self.cell( 0, 10, 'Primary Skills', ln=True )
        self.set_font( 'Arial', '', 10 )
        if type( details['primary_skills'] ) == str:
            for skills in details['primary_skills'].split( ',' ):
                skills = skills.encode( 'latin-1', 'replace' ).decode( 'latin-1' )
                self.cell( 0, 6, skills, ln=True )

        self.ln( 3 )
        self.set_font( 'Arial', 'BU', 12 )
        self.cell( 0, 10, 'Extra_activities', ln=True )
        self.set_font( 'Arial', '', 10 )
        extra_activities = details['extra_activities'].replace( "'", '' ).encode( 'latin-1', 'replace' ).decode(
            'latin-1' )
        self.cell( 0, 6, extra_activities, ln=True )

        self.ln( 3 )
        self.set_font( 'Arial', 'BU', 12 )
        self.cell( 0, 10, 'Job_title', ln=True )
        self.set_font( 'Arial', '', 10 )
        job_title = details['job_title'].encode( 'latin-1', 'replace' ).decode( 'latin-1' )
        self.cell( 0, 6, job_title, ln=True )

        self.ln( 3 )
        self.set_font( 'Arial', 'BU', 12 )
        self.cell( 0, 10, 'City:', ln=True )
        self.set_font( 'Arial', '', 10 )
        city = details['city'].encode( 'latin-1', 'replace' ).decode( 'latin-1' )
        self.multi_cell( 0, 5, city )

        self.set_y( self.get_y() - 14 )
        self.set_x( self.w - 90 )
        self.set_font( 'Arial', 'BU', 12 )
        self.cell( 0, 10, 'State:', ln=True )
        self.set_font( 'Arial', '', 10 )
        self.set_y( self.get_y() - 0 )
        self.set_x( self.w - 90 )
        state = details['state'].encode( 'latin-1', 'replace' ).decode( 'latin-1' )
        self.multi_cell( 0, 5, state )

        self.ln( 3 )
        self.set_font( 'Arial', 'BU', 12 )
        self.cell( 0, 10, 'Social_media_id:', ln=True )
        self.set_font( 'Arial', '', 10 )
        social_media_id = details['social_media_id'].encode( 'latin-1', 'replace' ).decode( 'latin-1' )
        self.multi_cell( 0, 5, social_media_id )

        self.set_y( self.get_y() - 14 )
        self.set_x( self.w - 90 )
        self.set_font( 'Arial', 'BU', 12 )
        self.cell( 0, 10, 'Linkedin_url:', ln=True )
        self.set_font( 'Arial', '', 10 )
        self.set_y( self.get_y() - 0 )
        self.set_x( self.w - 90 )
        url = details['linkedin_url'].replace( "'", '' ).encode( 'latin-1', 'replace' ).decode( 'latin-1' )
        self.multi_cell( 0, 5, url )

        # self.ln( 3 )
        # self.set_font( 'Arial', 'BU', 12 )
        # self.cell( 0, 10, 'Resume HTML Tag:', ln=True )
        # self.set_font( 'Arial', '', 10 )
        # tag = details['resume_html_tag'].encode( 'latin-1', 'replace' ).decode( 'latin-1' )
        # self.multi_cell( 0, 5, tag )
        #
        # self.set_y( self.get_y() - 14 )
        # self.set_x( self.w - 90 )
        # self.set_font( 'Arial', 'BU', 12 )
        # self.cell( 0, 10, 'Source:', ln=True )
        # self.set_font( 'Arial', '', 10 )
        # self.set_y( self.get_y() - 0 )
        # self.set_x( self.w - 90 )
        # source = details['source'].replace( "'", '' ).encode( 'latin-1', 'replace' ).decode( 'latin-1' )
        # self.multi_cell( 0, 5, source )


pdf = PDF()
pdf.add_page()
pdf.add_details( details )
pdf.output( 'resume.pdf' )
