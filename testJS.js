
console.log('Loaded');

$.getJSON("resume.json", function(resumeRawData) {

    objResume = resumeRawData;

    //Keys: basics/work/education/skills/languages
    for (let [key, value] of Object.entries(objResume)) {
      //console.log(`${key}: ${value}`);

      //Start aboutme & contacts
      if(key == "basics"){

        //Create object with basics
        objBasics = value;

        //Update Name
        document.getElementById("aboutmeName").innerHTML = objBasics['name'];

        //Update sublabel
        document.getElementById("aboutmeSubHeading").innerHTML = objBasics['label'];

        //Update description
        document.getElementById("aboutmeDescription").innerHTML = objBasics['summary'];

        //Format contact address
        varAddress = " " + objBasics["location"]['address'] + ", " +
                     objBasics["location"]['city'] +  ", " +
                     objBasics["location"]['region'];
        //Update contact address
        document.getElementById("contactAddress").innerHTML = varAddress;

        //Update contact phone number
        document.getElementById("contactPhone").innerHTML = " " + objBasics['phone'];

        //Update contact email
        varEmail = " " + "<a href=\"mailto:" + objBasics['email'] + "\">" +
              objBasics['email'] + "</a>"
        document.getElementById("contactEmail").innerHTML = varEmail;

        //Update contact website
        varWebsite = " " + "<a href=\"" + objBasics['website'] + "\">" +
              objBasics['website'] + "</a>"
        document.getElementById("contactWebsite").innerHTML = varWebsite;
      }
      //End aboutme & contacts

      //Start work experience
      if(key == "work"){
        //Create object with work
        arrayWork = value;

        //Loop through individual jobs
        for (job of arrayWork){

          //Get actions and store to display in HTML below
          var actionList = ['<ul>'];

          //Add lists from json to li element
          for (action of job['actions']){
            actionList.push( '<li>' + action + '</li>' )
          }
          actionList.push('</ul>')

          //Create temporary block of HTML
          var html = [
              '<div class="col-xs-12 col-sm-3 col-md-2 col-lg-2">',
                '<div class="workYear"><span class="prevY">' + job['endDate'] + '</span>',
                  '<span class="afterY">' + job['startDate'] + '</span></div>',
              '</div>',
              '<div class="col-xs-12 col-sm-9 col-md-10 col-lg-10 rightArea">',
                '<div class="arrowpart"></div>',
                '<div class="exCon">',
                  '<h4>' + job['company'] + '</h4>',
                  '<h5>' + job['position'] + '</h5>',
                  '<h5><small>' + job['summary'] + '</small></h5>',
                  '<div id="jobActions">',
                  actionList,
                  '</div>',
                '</div>',
              '</div>',
          ].join('');

          //Create div, add classes, add html, and add to parent div
          var div = document.createElement('div');
          div.setAttribute('class', 'row workDetails');
          div.innerHTML = html;
          document.getElementById('exprienceWork').appendChild(div);
        }
        //Done looping through individual jobs
      }
      //End work experience

      //Start education
      if(key == "education"){
        //Creat object with work
        arrayEdu = value;

        //Loop through individual schools
        for (edu of arrayEdu){

          //Create temporary block of HTML
          var html = [
            '<div class="col-xs-12 col-sm-3 col-md-2 col-lg-2">',
              '<div class="workYear"><span class="afterY">' + edu['endDate'] + '</span></div>',
            '</div>',
            '<div class="col-xs-12 col-sm-9 col-md-10 col-lg-10 rightArea">',
              '<div class="arrowpart"></div>',
              '<div class="exCon">',
                '<h4>' + edu['area'] + '</h4>',
                '<h5>' + edu['institution'] + '</h5>',
                '<p>' + edu['studyType'] + '</p>',
              '</div>',
            '</div>'
          ].join('');

          //Create div, add classes, add html, and add to parent div
          var div = document.createElement('div');
          div.setAttribute('class', 'row workDetails');
          div.innerHTML = html;
          document.getElementById('educationSchools').appendChild(div);

        }
        //Done looping though individual schools
      }
      //End education

      //Start skills
      if(key == "skills"){
        //Creat object with skill
        arraySkills = value;

        //Loop through individual skills
        for (skill of arraySkills){

          //Create temporary block of HTML
          var html = [
            '<div class="col-xs-12 skills">',
              '<span class="chart skilBg" data-percent=\"' + skill['level'] + '\"> <span class="percent"></span> </span>',
              '<h4>' + skill['name'] + '</h4>',
              '<p><small><i>' + skill['keywords'] + '</i></small></p>',
              '<p>' + skill['summary'] + '</p>',
            '</div>'
          ].join('');

          //Create div, add classes, add html, and add to parent div
          var div = document.createElement('div');
          div.setAttribute('class', 'col-xs-12 col-sm-6 col-md-6 col-lg-6 skillsArea');
          div.innerHTML = html;
          document.getElementById('jobSkills').appendChild(div);

        }
        //End individual skills
      }
      //End skills

      //Start aboutme & contacts
      if(key == "languages"){

        //Create object with basics
        objBasics = value[0];

        console.log(objBasics)

        //Update Name
        document.getElementById("langaugeSpoken").innerHTML = objBasics['fluencySpoken'];

        //Update written
        document.getElementById("languageWritten").innerHTML = objBasics['fluencyWritten'];
      }

    }
    //End Keys
});
