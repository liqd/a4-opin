/*------------------------------*
 *      Googe maps functions
 *------------------------------*/

  var map;
  var drawingManager;
  var selectedShape;
  var colors = ['#1E90FF', '#FF1493', '#32CD32', '#FF8C00', '#4B0082'];
  var selectedColor;
  var colorButtons = {};
  var defaultLatLng;
  var initialGeofenceLocation;

  function clearSelection() {
    if (selectedShape) {
      selectedShape.setEditable(false);
      selectedShape = null;
    }
  }

  function setSelection(shape) {
    clearSelection();
    selectedShape = shape;
    shape.setEditable(true);
    selectColor(shape.get('fillColor') || shape.get('strokeColor'));
  }

  function deleteSelectedShape() {
    if (selectedShape) {
      selectedShape.setMap(null);
    }
    // To show:
     drawingManager.setOptions({
       drawingControl: true
     });

    // Editing geolocation field
    var elem = document.getElementById("geofenceLocation");
    elem.parentNode.removeChild(elem);

    var geofenceKey = '<input type="hidden" id="geofenceLocation" name="module_settings-geofenceLocation" value=""/>';
    document.getElementById("field-hide").innerHTML += geofenceKey;
  }

  function restoreShape() {
    if (selectedShape) {
      selectedShape.setMap(null);
    }
    selectedShape.setMap(null);
    drawLocation(initialGeofenceLocation);

    // Editing geolocation field
    var elem = document.getElementById("geofenceLocation");
    elem.parentNode.removeChild(elem);

    var geofenceKey = '<input type="hidden" id="geofenceLocation" name="module_settings-geofenceLocation" value="'+initialGeofenceLocation+'""/>';
    document.getElementById("field-hide").innerHTML += geofenceKey;


    // To show:
     drawingManager.setOptions({
       drawingControl: true
     });
  }

  function selectColor(color) {
    selectedColor = color;
    for (var i = 0; i < colors.length; ++i) {
      var currColor = colors[i];
      colorButtons[currColor].style.border = currColor == color ? '2px solid #789' : '2px solid #fff';
    }

    // Retrieves the current options from the drawing manager and replaces the
    // stroke or fill color as appropriate.
    var polylineOptions = drawingManager.get('polylineOptions');
    polylineOptions.strokeColor = color;
    drawingManager.set('polylineOptions', polylineOptions);

    var rectangleOptions = drawingManager.get('rectangleOptions');
    rectangleOptions.fillColor = color;
    drawingManager.set('rectangleOptions', rectangleOptions);

    var circleOptions = drawingManager.get('circleOptions');
    circleOptions.fillColor = color;
    drawingManager.set('circleOptions', circleOptions);

    var polygonOptions = drawingManager.get('polygonOptions');
    polygonOptions.fillColor = color;
    drawingManager.set('polygonOptions', polygonOptions);
  }

  function setSelectedShapeColor(color) {
    if (selectedShape) {
      if (selectedShape.type == google.maps.drawing.OverlayType.POLYLINE) {
        selectedShape.set('strokeColor', color);
      } else {
        selectedShape.set('fillColor', color);
      }
    }
  }

  function makeColorButton(color) {
    var button = document.createElement('span');
    button.className = 'color-button';
    button.style.backgroundColor = color;
    google.maps.event.addDomListener(button, 'click', function() {
      selectColor(color);
      setSelectedShapeColor(color);
    });

    return button;
  }

   function buildColorPalette() {
     var colorPalette = document.getElementById('color-palette');
     for (var i = 0; i < colors.length; ++i) {
       var currColor = colors[i];
       var colorButton = makeColorButton(currColor);
       colorPalette.appendChild(colorButton);
       colorButtons[currColor] = colorButton;
     }
     selectColor(colors[0]);
   }

/* create a location with the supplied infomation and do clean after receiving the request response
*/
function create_location (){

    var wktFormat = trans_to_wkt(selectedShape.getPath().b);
    selectedShape.setMap(null);
    drawLocation(wktFormat);

    // Editing geolocation field
    var elem = document.getElementById("geofenceLocation");
    elem.parentNode.removeChild(elem);

    var geofenceKey = '<input type="hidden" id="geofenceLocation" name="module_settings-geofenceLocation" value="'+wktFormat+'""/>';
    document.getElementById("field-hide").innerHTML += geofenceKey;

}

/* draw a location at the map and center the map by its geographic coordinates
 * param (location : object) : the location object
*/
function drawLocation(location) {
    var center = drawPolygon(location)[0];

    //if(center.lat() && center.lng()) {
    if(center) {
        map.setCenter(center);
        if (map.getZoom() < 5) map.setZoom(7);
    }else {
        map.setCenter(defaultLatLng);
    }
}


function drawPolygon(wktFormat) {
    var polygon = trans_to_array(wktFormat);

    selectedShape = new google.maps.Polygon({
        paths: polygon,
        strokeColor: colors[0],
        strokeOpacity: 0.6,
        strokeWeight: 0,
        fillColor: colors[0],
        fillOpacity: 0.45,
        editable: true
    });



    selectedShape.setMap(map);

    return polygon;
}


function trans_to_wkt(paths) {

    var res = "POLYGON((";
    for (var j = 0; j < paths.length; j++) {
        res = res + paths[j].lng() + " " + paths[j].lat() + ","
    };
    res = res + paths[0].lng() + " " + paths[0].lat() + "))";
    return res;
}

function trans_to_array(wkt){
    //initialize wkt-textarea-input
    var res = [], coors;

    var input_cache = wkt.replace('POLYGON((','');
    input_cache = input_cache.replace('))','');

    var input_array = input_cache.split(',')

    for (var j = 0; j < input_array.length - 1; j++) {
        coors = input_array[j].trim().split(" ");
        res.push(new google.maps.LatLng(parseFloat(coors[1]), parseFloat(coors[0])));
    }

    return res;
}

window.initialize = function(){
    defaultLatLng = new google.maps.LatLng(52.520, 13.404);
    map = new google.maps.Map(document.getElementById('map'), {
      //zoom: 10,
      zoom: 4,
      center: new google.maps.LatLng(22.344, 114.048),
      mapTypeId: google.maps.MapTypeId.ROADMAP,
      disableDefaultUI: true,
      zoomControl: true
    });

    $('.tabs a[href="#participation"]').click(function(){
       $(this).tab('show');
       initialize();
    });

    var polyOptions = {
      strokeWeight: 0,
      fillOpacity: 0.45,
      editable: true
    };
    // Creates a drawing manager attached to the map that allows the user to draw
    // markers, lines, and shapes.
    drawingManager = new google.maps.drawing.DrawingManager({
      drawingMode: google.maps.drawing.OverlayType.POLYGON,
      drawingControlOptions: {
        drawingModes: [
          google.maps.drawing.OverlayType.POLYGON
        ]
      },
      markerOptions: {
        draggable: true
      },
      polylineOptions: {
        editable: true
      },
      rectangleOptions: polyOptions,
      circleOptions: polyOptions,
      polygonOptions: polyOptions,
      map: map
    });

    google.maps.event.addListener(drawingManager, 'overlaycomplete', function(event) {
      if (event.type == google.maps.drawing.OverlayType.CIRCLE) {
        var radius = event.overlay.getRadius();
      }
    });
    google.maps.event.addListener(drawingManager, 'overlaycomplete', function(e) {
        if (e.type != google.maps.drawing.OverlayType.MARKER) {
        // Switch back to non-drawing mode after drawing a shape.
        drawingManager.setDrawingMode(null);
        // To hide:
        drawingManager.setOptions({
          drawingControl: false
        });

        // Add an event listener that selects the newly-drawn shape when the user
        // mouses down on it.
        var newShape = e.overlay;
        newShape.type = e.type;
        google.maps.event.addListener(newShape, 'click', function() {
          setSelection(newShape);
        });
        setSelection(newShape);
        create_location ();
      }
    });

    var key = "geofenceLocation"
    var geofenceLocation = document.getElementById(key).value;

    if(!geofenceLocation){
        map.setCenter(defaultLatLng);
    }else{
        drawLocation(geofenceLocation);
        initialGeofenceLocation = geofenceLocation;
        //var newShape = geofenceLocation;
        //newShape.type = "poly";
       // setSelection(newShape);
    }

    // Clear the current selection when the drawing mode is changed, or when the
    // map is clicked.
    google.maps.event.addListener(drawingManager, 'drawingmode_changed', clearSelection);
    google.maps.event.addListener(map, 'click', clearSelection);
    google.maps.event.addDomListener(document.getElementById('delete-button'), 'click', deleteSelectedShape);
    google.maps.event.addDomListener(document.getElementById('restore-button'), 'click', restoreShape);

    buildColorPalette();
  }
  //google.maps.event.addDomListener(window, 'load', initialize);



  /*------------------------------------*
 *      Build the on-ready callback
 *------------------------------------*/
document.addEventListener('DOMContentLoaded', function () {
  if (document.querySelectorAll('#map').length > 0)
  {
    var js_file = document.createElement('script');
    js_file.type = 'text/javascript';
    js_file.src = 'http://maps.googleapis.com/maps/api/js?key=AIzaSyC8kq3VbEzLA1xqe0ItRk-y4bgAg89h4Qc&callback=initialize&v=3&sensor=true&libraries=drawing';
    document.getElementsByTagName('head')[0].appendChild(js_file);
  }
});



/* -----------------------*
 * Flashpoll functions
 * -----------------------*/


/* Remove a choice from collection
 * param (choices array) : choice collection of question
 * param (choice object) : choice object to be removed from collection
 * param (string key) : html element's key
*/
window.removeChoice = function(choices, qcorderIdIn, qorderId, key){
//function removeChoice(choices, qcorderIdIn, qorderId, key) {
	if(choices.length>1) {
        var index,ind;
        for(var i=0;i<choices.length;i++){
            if(choices[i].orderId == qcorderIdIn){
                index = i;
                break;
            }

        }
			choices.splice(index,1);

		// update the position value of choice by starting at "index"
		for(ind=index;ind<choices.length;ind++)
			choices[ind].position=ind+1;

    var elem = document.getElementById(key);
    var parent = elem.parentNode;
    elem.parentNode.removeChild(elem);

    // update the Dom elements
    var qcorderId = 1;
    $(parent).children().each(function(){
		if($(this).children()[1] && $(this).children()[1].children[0] )	{
			$(this).attr('id','form-group-question-'+qorderId+'.choice-'+qcorderId);
			$(this).children()[0].innerHTML = 'Choice '+qcorderId;

			$(this).children()[1].children[0].children[0].id = 'id_module_settings-question_'+qorderId+'_choice_'+qcorderId+'_answerText';
			$(this).children()[1].children[0].children[0].name = 'module_settings-question_'+qorderId+'_choice_'+qcorderId+'_answerText';


			var formkey ='form-group-question-'+qorderId+'.choice-'+qcorderId;
			$(this).children()[1].children[1].children[0].onclick = function(){ removeChoice(choices, qcorderId, qorderId, formkey); };

			qcorderId++;
		}
	});


	var remvkey = "icon-plus-question-"+qorderId;
    var elem = document.getElementById(remvkey);
	elem.parentNode.removeChild(elem);

	var pluskey= '<div id="icon-plus-question-'+qorderId+'" class="span3">'+
		'<div class="fa fa-plus fa-2x" tooltip="Ajouter un choix" tooltip-trigger="mouseenter" tooltip-placement="left" tooltip-popup-delay="1000" onclick=\'addChoice('+JSON.stringify(choices)+','+qorderId+',"fp-phase-qc-'+qorderId+'")\' tabindex="-1" style="float:left;"></div>'+
		'<div style="clear:both;"></div>'+
	'</div>';

	var d = document.createElement('div');
	d.innerHTML = pluskey;

	parent.appendChild(d.firstChild);

}

    return false;

};


/* Remove a question from collection
 * param (questions array) : question collection of question
 * param (question object) : question object to be removed from collection
 * param (string key) : html element's key
*/

window.removeQuestion = function(questions,qorderIdIn,key) {
//function removeQuestion(questions,qorderIdIn,key) {
	if(questions.length>1) {
        var index,ind;
        for(var i=0;i<questions.length;i++){
            if(questions[i].orderId == qorderIdIn){
                index = i;
                break;
            }
        }

		questions.splice(index,1);
		// update the position value of question by starting at "index"
		for(ind=index;ind<questions.length;ind++)
			questions[ind].position=ind+1;
	}

    var elem = document.getElementById(key);
    var parent = elem.parentNode;
    elem.parentNode.removeChild(elem);

    // update the Dom elements
    var qorderId = 1;
    $(parent).children().each(function(){
		if($(this).children()[1] && $(this).children()[1].children[0])	{
			$(this).attr('id','form-group-question-'+qorderId);

			// Titre - $(this).children()[0]
			$(this).children()[0].children[0].innerHTML = 'Question '+qorderId;

			$(this).children()[0].children[1].children[0].children[0].id = 'id_module_settings-question_'+qorderId+'_questionText';
			$(this).children()[0].children[1].children[0].children[0].name = 'module_settings-question_'+qorderId+'_questionText';

			var formkey ='form-group-question-'+qorderId;
			$(this).children()[0].children[1].children[1].children[0].onclick = function(){ removeQuestion(questions, qorderId, formkey); };

			// Type - $(this).children()[1]
			//$(this).children()[1].children[1].id = 'id_module_settings-question_'+qorderId+'_questionType';
			//$(this).children()[1].children[1].name = 'module_settings-question_'+qorderId+'_questionType';
            var value;
            if($(this).children()[1].children[1]){
                value = $(this).children()[1].children[1].value
            }
            var selectKey =            '<label>'+
                'Type'+
                '<br>'+
            '</label>'+
            '<select class="form-control select" id="id_module_settings-question_'+qorderId+'_questionType" name="module_settings-question_'+qorderId+'_questionType"  onchange=\'changeType(this.options[this.selectedIndex].value, "fp-phase-qc-'+qorderId+'", '+qorderId+')\' >';
                if(value =='CHECKBOX')
                    selectKey = selectKey +'<option value="CHECKBOX"  selected>MULTIPLE</option>';
                else
                    selectKey = selectKey +'<option value="CHECKBOX">MULTIPLE</option>';

                if(value =='RADIO')
                    selectKey = selectKey +'<option value="RADIO" selected>SINGLE</option>';
                else
                    selectKey = selectKey +'<option value="RADIO" >SINGLE</option>';

                if(value =='FREETEXT')
                    selectKey = selectKey +'<option value="FREETEXT"  selected>OPEN</option>';
                else
                    selectKey = selectKey +'<option value="FREETEXT"  >OPEN</option>';

                if(value =='ORDER')
                    selectKey = selectKey +'<option value="ORDER"  selected>RANKING</option>';
                else
                    selectKey = selectKey +'<option value="ORDER"  >RANKING</option>';

            selectKey = selectKey +'</select>';

            $(this).children()[1].innerHTML = selectKey;


			// Mandatory - $(this).children()[2]
			$(this).children()[2].children[0].children[0].id = 'id_module_settings-question_'+qorderId+'_mandatory';
			$(this).children()[2].children[0].children[0].name = 'module_settings-question_'+qorderId+'_mandatory';

            if($(this).children()[3]){
                // Choices - $(this).children()[3]
                $(this).children()[3].id = 'fp-phase-qc-'+qorderId;
                var node = $(this).children()[3];
                // update the Dom elements
                var qcorderId = 1;
                var answers = questions[qorderId-1].answers;
                $(node).children().each(function(){
                    if($(this).children()[1] && $(this).children()[1].children[0])	{
                        $(this).attr('id','form-group-question-'+qorderId+'.choice-'+qcorderId);
                        $(this).children()[0].innerHTML = 'Choice '+qcorderId;

                        $(this).children()[1].children[0].children[0].id = 'id_module_settings-question_'+qorderId+'_choice_'+qcorderId+'_answerText';
                        $(this).children()[1].children[0].children[0].name = 'module_settings-question_'+qorderId+'_choice_'+qcorderId+'_answerText';

                        var formkey ='form-group-question-'+qorderId+'.choice-'+qcorderId;
                        var orderId = qcorderId;
                        var orderIdQ = qorderId;
                        $(this).children()[1].children[1].children[0].onclick = function(){ removeChoice(answers, orderId, orderIdQ, formkey); };

                        qcorderId++;
                    }else{
                        $(this).attr('id','icon-plus-question-'+qorderId);
                        var formkey ='fp-phase-qc-'+qorderId;
                        var orderId = qorderId;
                        $(this).children()[0].onclick = function(){ addChoice(answers, orderId, formkey); };
                    }
                });
            }

			qorderId++;
		}
	});



	var remvkey = "icon-plus-poll";
    var elem = document.getElementById(remvkey);
	elem.parentNode.removeChild(elem);

    var pluskey = '<div id="icon-plus-poll" class="span3">'+
            '<div class="btn btn-success ng-binding" onclick=\'addQuestion('+JSON.stringify(questions)+',"fp-phase-2")\' tabindex="-1"><i class="fa fa-plus"></i>&nbsp;Add a question</div>'+
            '<div style="clear:both;"></div>'+
        '</div>';


	var d = document.createElement('div');
	d.innerHTML = pluskey;

	parent.appendChild(d.firstChild);

    return false;
};



/* Add a choice to collection
 * param (choices array) : choice collection of question
 * param (int questionPos) : position of the question
 * param (string key) : html element's key
*/
window.addChoice = function(choices,questionPos, key) {
//function addChoice(choices,questionPos, key) {
    var choice;
	if (choices[choices.length-1].freetextAnswer) {
	    choice = {"answerText":"","orderId":choices.length,"mediaURL":"","freetextAnswer":false};
		choices.splice(length-1, 0, choice);
	}else {
	    choice = {"answerText":"","orderId":choices.length+1,"mediaURL":"","freetextAnswer":false};
		choices.push(choice);
	}

    // Remove the button
    var remvkey = "icon-plus-question-"+questionPos;
    var elem = document.getElementById(remvkey);
	var parent = elem.parentNode;
    parent.removeChild(elem);

    var choiceKey = '<div id="form-group-question-'+questionPos+'.choice-'+choice.orderId+'" class="form-group">'+
            '<label>'+
                'Choice '+choice.orderId+
                '<br>'+
            '</label>'+
            '<div style="position:relative;">'+
                '<div style="margin-right: 44px;">'+
                    '<input class="form-control choice" id="id_module_settings-question_'+questionPos+'_choice_'+choice.orderId+'_answerText" maxlength="800" name="module_settings-question_'+questionPos+'_choice_'+choice.orderId+'_answerText" type="text" value="" />'+
                '</div>'+
                '<div style="width: 39px;position:absolute;right:0;height:100%;top:0;">'+
                    '<i class="fa fa-times fa-2x" tooltip="Supprimer" tooltip-trigger="mouseenter" tooltip-placement="left" tooltip-popup-delay="1000" onclick=\'removeChoice('+JSON.stringify(choices)+','+choice.orderId+','+questionPos+',"form-group-question-'+questionPos+'.choice-'+choice.orderId+'")\' ng-disabled="question.questionChoices.length<=2" tabindex="-1" disabled="disabled"></i>'+
                '</div>'+
            '</div>'+
        '</div>';

    var choiceKey2 = '<div id="icon-plus-question-'+questionPos+'" class="span3">'+
			'<div class="fa fa-plus fa-2x" tooltip="Ajouter un choix" tooltip-trigger="mouseenter" tooltip-placement="left" tooltip-popup-delay="1000" onclick=\'addChoice('+JSON.stringify(choices)+','+questionPos+',"fp-phase-qc-'+questionPos+'")\' tabindex="-1" style="float:left;"></div>'+
			'<div style="clear:both;"></div>'+
		'</div>';

	var d = document.createElement('div');
	d.innerHTML = choiceKey;

	var d2 = document.createElement('div');
	d2.innerHTML = choiceKey2;

	document.getElementById(key).appendChild(d.firstChild);
	document.getElementById(key).appendChild(d2.firstChild);
	// Reorder
    // update the Dom elements
    var qcorderId = 1;
	var qorderId = questionPos;
    $(parent).children().each(function(){
		if($(this).children()[1] && $(this).children()[1].children[0])	{
			$(this).attr('id','form-group-question-'+qorderId+'.choice-'+qcorderId);
			$(this).children()[0].innerHTML = 'Choice '+qcorderId;

			$(this).children()[1].children[0].children[0].id = 'id_module_settings-question_'+qorderId+'_choice_'+qcorderId+'_answerText';
			$(this).children()[1].children[0].children[0].name = 'module_settings-question_'+qorderId+'_choice_'+qcorderId+'_answerText';


			var formkey ='form-group-question-'+qorderId+'.choice-'+qcorderId;
			$(this).children()[1].children[1].children[0].onclick = function(){ removeChoice(choices, qcorderId, qorderId, formkey); };

			qcorderId++;
		}
	});
};



/* Add a question to collection
 * param (questions array) : choice collection of question
 * param ($event object) : event object
*/
window.addQuestion = function(questions, key) {
//function addQuestion(questions, key) {
    if(!questions){
        var questions = [];
    }
    var question = {"questionText":"","orderId":questions.length+1,"questionType":"CHECKBOX","mandatory":true,"mediaURLs":[""],"answers":[{"answerText":"","orderId":1,"mediaURL":"","freetextAnswer":false},{"answerText":"","orderId":2,"mediaURL":"","freetextAnswer":false}]};
	questions.push(question);

    // Remove the button
    var remvkey = "icon-plus-poll";
    var elem = document.getElementById(remvkey);
	var parent = elem.parentNode;
    parent.removeChild(elem);

	var questionKey ='<div id="form-group-question-'+question.orderId+'">'+
        '<div class="form-group">'+
            '<label>'+
                'Question '+question.orderId+
                '<br>'+
            '</label>'+
            '<div style="position:relative;">'+
                '<div style="margin-right: 44px;">'+
                   '<input class="form-control choice" id="id_module_settings-question_'+question.orderId+'_questionText" name="module_settings-question_'+question.orderId+'_questionText" type="text" value="" maxlength="800" />'+
                '</div>'+
                '<div style="width: 39px;position:absolute;right:0;height:100%;top:0;">'+
                    '<i class="fa fa-trash-o fa-2x" tooltip="Supprimer" tooltip-popup-delay="1000" tooltip-trigger="mouseenter" tooltip-placement="left" onclick=\'removeQuestion('+JSON.stringify(questions)+','+question.orderId+', "form-group-question-'+question.orderId+'")\' tabindex="-1"></i>'+
                '</div>'+
            '</div>'+
        '</div>'+
        '<div class="form-group">'+
            '<label>'+
                'Type'+
                '<br>'+
            '</label>'+
            '<select class="form-control select" id="id_module_settings-question_'+question.orderId+'_questionType" name="module_settings-question_'+question.orderId+'_questionType"  onchange=\'changeType(this.options[this.selectedIndex].value, "fp-phase-qc-'+question.orderId+'", '+question.orderId+')\' >'+
                '<option value="CHECKBOX"  selected>MULTIPLE</option>'+
                '<option value="RADIO" >SINGLE</option>'+
                '<option value="FREETEXT" >OPEN</option>'+
                '<option value="ORDER"  >RANKING</option>'+
            '</select>'+
        '</div>'+
        '<div class="form-group ">'+
            '<label>'+
                '<input id="id_module_settings-question_'+question.orderId+'_mandatory" name="module_settings-question_'+question.orderId+'_mandatory" type="checkbox" value="" checked="checked" />'+
                'Mandatory'+
                '<br>'+
            '</label>'+
        '</div>'+
		'<div id="fp-phase-qc-'+question.orderId+'">';
        for(var ind=0;ind<question.answers.length;ind++){
            var answer = question.answers[ind];
            questionKey = questionKey +'<div id="form-group-question-'+question.orderId+'.choice-'+answer.orderId+'" class="form-group">'+
                '<label>'+
                    'Choice '+answer.orderId+
                    '<br>'+
                '</label>'+
                '<div style="position:relative;">'+
                    '<div style="margin-right: 44px;">'+
                        '<input class="form-control choice" id="id_module_settings-question_'+question.orderId+'_choice_'+answer.orderId+'_answerText" maxlength="800" name="module_settings-question_'+question.orderId+'_choice_'+answer.orderId+'_answerText" type="text" value="" />'+
                    '</div>'+
                    '<div style="width: 39px;position:absolute;right:0;height:100%;top:0;">'+
                        '<i class="fa fa-times fa-2x" tooltip="Supprimer" tooltip-trigger="mouseenter" tooltip-placement="left" tooltip-popup-delay="1000" onclick=\'removeChoice('+JSON.stringify(question.answers)+','+answer.orderId+','+question.orderId+', "form-group-question-'+question.orderId+'.choice-'+answer.orderId+'")\' ng-disabled="question.questionChoices.length<=2" tabindex="-1" disabled="disabled"></i>'+
                    '</div>'+
                    '</div>'+
                '</div>';

                if (answer.orderId == question.answers.length){
                    questionKey = questionKey +
                    '<div id="icon-plus-question-'+question.orderId+'" class="span3">'+
                        '<div class="fa fa-plus fa-2x" tooltip="Ajouter un choix" tooltip-trigger="mouseenter" tooltip-placement="left" tooltip-popup-delay="1000" onclick=\'addChoice('+JSON.stringify(question.answers)+','+question.orderId+', "fp-phase-qc-'+question.orderId+'")\' tabindex="-1" style="float:left;"></div>'+
                        '<div style="clear:both;"></div>'+
                    '</div>';
                }
        }

    questionKey = questionKey +'</div>'+
				'</div>';

    var questionKey1 = '<div id="icon-plus-poll" class="span3">'+
            '<div class="btn btn-success ng-binding" onclick=\'addQuestion('+JSON.stringify(questions)+',"fp-phase-2")\' tabindex="-1"><i class="fa fa-plus"></i>&nbsp;Add a question</div>'+
            '<div style="clear:both;"></div>'+
        '</div>';

	var d = document.createElement('div');
	d.innerHTML = questionKey;

	var d1 = document.createElement('div');
	d1.innerHTML = questionKey1;

	document.getElementById(key).appendChild(d.firstChild);
	document.getElementById(key).appendChild(d1.firstChild);

	var parent = document.getElementById(key);

    // update the Dom elements
    var qorderId = 1;
    $(parent).children().each(function(){
		if($(this).children()[1] && $(this).children()[1].children[0])	{
			$(this).attr('id','form-group-question-'+qorderId);

			// Titre - $(this).children()[0]
			$(this).children()[0].children[0].innerHTML = 'Question '+qorderId;
			$(this).children()[0].children[1].children[0].children[0].id = 'id_module_settings-question_'+qorderId+'_questionText';
			$(this).children()[0].children[1].children[0].children[0].name = 'module_settings-question_'+qorderId+'_questionText';

			var formkey ='form-group-question-'+qorderId;
			$(this).children()[0].children[1].children[1].children[0].onclick = function(){ removeQuestion(questions, qorderId, formkey); };

			// Type - $(this).children()[1]
			//$(this).children()[1].children[1].id = 'id_module_settings-question_'+qorderId+'_questionType';
			//$(this).children()[1].children[1].name = 'module_settings-question_'+qorderId+'_questionType';

            var value;
            if($(this).children()[1].children[1]){
                value = $(this).children()[1].children[1].value
            }

            var selectKey ='<label>'+
                'Type'+
                '<br>'+
            '</label>'+
            '<select class="form-control select" id="id_module_settings-question_'+qorderId+'_questionType" name="module_settings-question_'+qorderId+'_questionType"  onchange=\'changeType(this.options[this.selectedIndex].value, "fp-phase-qc-'+qorderId+'", '+qorderId+')\' >';
                if(value =='CHECKBOX')
                    selectKey = selectKey +'<option value="CHECKBOX"  selected>MULTIPLE</option>';
                else
                    selectKey = selectKey +'<option value="CHECKBOX">MULTIPLE</option>';

                if(value =='RADIO')
                    selectKey = selectKey +'<option value="RADIO" selected>SINGLE</option>';
                else
                    selectKey = selectKey +'<option value="RADIO" >SINGLE</option>';

                if(value =='FREETEXT')
                    selectKey = selectKey +'<option value="FREETEXT"  selected>OPEN</option>';
                else
                    selectKey = selectKey +'<option value="FREETEXT"  >OPEN</option>';

                if(value =='ORDER')
                    selectKey = selectKey +'<option value="ORDER"  selected>RANKING</option>';
                else
                    selectKey = selectKey +'<option value="ORDER"  >RANKING</option>';

            selectKey = selectKey +'</select>';

            $(this).children()[1].innerHTML = selectKey;

			// Mandatory - $(this).children()[2]
			$(this).children()[2].children[0].children[0].id = 'id_module_settings-question_'+qorderId+'_mandatory';
			$(this).children()[2].children[0].children[0].name = 'module_settings-question_'+qorderId+'_mandatory';


            if($(this).children()[3]){
			// Choices - $(this).children()[3]
			$(this).children()[3].id = 'fp-phase-qc-'+qorderId;
			var node = $(this).children()[3];
			// update the Dom elements
			var qcorderId = 1;
			var answers = questions[qorderId-1].answers;
			$(node).children().each(function(){
				if($(this).children()[1] && $(this).children()[1].children[0])	{
					$(this).attr('id','form-group-question-'+qorderId+'.choice-'+qcorderId);
					$(this).children()[0].innerHTML = 'Choice '+qcorderId;
                    $(this).children()[1].children[0].children[0].id = 'id_module_settings-question_'+qorderId+'_choice_'+qcorderId+'_answerText';
                    $(this).children()[1].children[0].children[0].name = 'module_settings-question_'+qorderId+'_choice_'+qcorderId+'_answerText';


					var formkey ='form-group-question-'+qorderId+'.choice-'+qcorderId;
					var orderId = qcorderId;
					var orderIdQ = qorderId;
					$(this).children()[1].children[1].children[0].onclick = function(){ removeChoice(answers, orderId, orderIdQ, formkey); };

					qcorderId++;
				}else{
					$(this).attr('id','icon-plus-question-'+qorderId);
					var formkey ='fp-phase-qc-'+qorderId;
					var orderId = qorderId;
					$(this).children()[0].onclick = function(){ addChoice(answers, orderId, formkey); };
				}
			});
        }
			qorderId++;
		}
	});


};

/* Update the appearance of question when the question type is changed
*/
window.changeType = function(questionType, key, qorderId) {
//function changeType(questionType, key, qorderId) {
    var elem = document.getElementById(key);
	if(questionType === 'FREETEXT') {
			$(elem).children().each(function(){
                elem.removeChild(this);
			});
	}else {
		if($(elem).children().length == 0){
            var question = {"questionText":"","orderId":qorderId,"questionType":"CHECKBOX","mandatory":true,"mediaURLs":[""],"answers":[{"answerText":"","orderId":1,"mediaURL":"","freetextAnswer":false},{"answerText":"","orderId":2,"mediaURL":"","freetextAnswer":false}]};
            var questionKey="";
                for(var ind=0;ind<question.answers.length;ind++){
                    var answer = question.answers[ind];
                    questionKey = '<div id="form-group-question-'+question.orderId+'.choice-'+answer.orderId+'" class="form-group">'+
                        '<label>'+
                            'Choice '+answer.orderId+
                            '<br>'+
                        '</label>'+
                        '<div style="position:relative;">'+
                            '<div style="margin-right: 44px;">'+
                                '<input class="form-control choice" id="id_module_settings-question_'+question.orderId+'_choice_'+answer.orderId+'_answerText" maxlength="800" name="module_settings-question_'+question.orderId+'_choice_'+answer.orderId+'_answerText" type="text" value="" />'+
                            '</div>'+
                            '<div style="width: 39px;position:absolute;right:0;height:100%;top:0;">'+
                                '<i class="fa fa-times fa-2x" tooltip="Supprimer" tooltip-trigger="mouseenter" tooltip-placement="left" tooltip-popup-delay="1000" onclick=\'removeChoice('+JSON.stringify(question.answers)+','+answer.orderId+','+question.orderId+', "form-group-question-'+question.orderId+'.choice-'+answer.orderId+'")\' ng-disabled="question.questionChoices.length<=2" tabindex="-1" disabled="disabled"></i>'+
                            '</div>'+
                            '</div>'+
                        '</div>';

                        if(document.getElementById(key)==null){
                            var upkey ='form-group-question-'+ qorderId;
                            questionKey ='<div id="fp-phase-qc-'+qorderId+'">' +
                                          questionKey +
                                         '</div>';

                            var d = document.createElement('div');
                            d.innerHTML = questionKey;
                            document.getElementById(upkey).appendChild(d.firstChild);
                        }else{
                            var d = document.createElement('div');
                            d.innerHTML = questionKey;
                            document.getElementById(key).appendChild(d.firstChild);
                        }

                        if (answer.orderId == question.answers.length){
                            questionKey ='<div id="icon-plus-question-'+question.orderId+'" class="span3">'+
                                '<div class="fa fa-plus fa-2x" tooltip="Ajouter un choix" tooltip-trigger="mouseenter" tooltip-placement="left" tooltip-popup-delay="1000" onclick=\'addChoice('+JSON.stringify(question.answers)+','+question.orderId+', "fp-phase-qc-'+question.orderId+'")\' tabindex="-1" style="float:left;"></div>'+
                                '<div style="clear:both;"></div>'+
                            '</div>';
                            var d = document.createElement('div');
                            d.innerHTML = questionKey;
                            document.getElementById(key).appendChild(d.firstChild);

                        }
                }
        }
    }
}
