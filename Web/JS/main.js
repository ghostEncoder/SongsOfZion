function ClearFullOutputTextBoxes()
{
    $("#FullOutputTextArea").val('');
}


//Function to print full song preview
function PrintFullSong(Song)
{   
    ClearFullOutputTextBoxes()
    //Iterater through full song
    console.log("INIDE PRINT FULL SONG")
    Song.forEach(function(value)
    {
        console.log(value)
        //iterate thorugh each verse
        value.forEach(function(verses)
        {
            //keep appending verses
            $("#FullOutputTextArea").val($("#FullOutputTextArea").val()+verses);
        })
         //add newline
        $("#FullOutputTextArea").val($("#FullOutputTextArea").val()+"\n");
    })
}

//Function to submit song
function SubmitSongNumber()
{
    var song_number = document.getElementById("SongNumberTamil").value;
    console.log(song_number.trim())
    eel.Search_Song(song_number)(function(ret){
        console.log(ret)
        
        let response = ret
        if (response === "No_Song_Error")
        {
            $('#error-modal').modal('show'); 
        }
        else
        {
            PrintFullSong(ret)
        }
    });
   
    
}

//Function to submit verses
function SubmitVerses()
{
    var stanzas=[]
    if(document.getElementById("chorus").checked)
    {
        stanzas.push(0);
    }
    if(document.getElementById("stanza-1").checked)
    {
        stanzas.push(1);
    }
    if(document.getElementById("stanza-2").checked)
    {
        stanzas.push(2);
    }
    if(document.getElementById("stanza-3").checked)
    {
        stanzas.push(3);
    }
    if(document.getElementById("stanza-4").checked)
    {
        stanzas.push(4);
    }
    if(document.getElementById("stanza-5").checked)
    {
        stanzas.push(5);
    }
    if(document.getElementById("stanza-6").checked)
    {
        stanzas.push(6);
    }
    if(document.getElementById("stanza-7").checked)
    {
        stanzas.push(7);
    }
    if(document.getElementById("stanza-8").checked)
    {
        stanzas.push(8);
    }
    if(document.getElementById("stanza-9").checked)
    {
        stanzas.push(9);
    }
    if(document.getElementById("stanza-10").checked)
    {
        stanzas.push(10);
    }
    if(document.getElementById("stanza-11").checked)
    {
        stanzas.push(11);
    }
    if(document.getElementById("stanza-12").checked)
    {
        stanzas.push(12);
    }
    if(document.getElementById("stanza-13").checked)
    {
        stanzas.push(13);
    }
    if(document.getElementById("stanza-12").checked)
    {
        stanzas.push(12);
    }
    if(document.getElementById("stanza-15").checked)
    {
        stanzas.push(12);
    }
    eel.GetVersesToBePrinted(stanzas)
}