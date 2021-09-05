//Function to open about modal
function OpenAboutModal()
{
    $('#about-modal').modal('show'); 
}

//Function to open version modal
function OpenVersionModal()
{
    $('#version-modal').modal('show'); 
}

//Function to reset everything
function Reset()
{
    eel.Reset();
    location.reload()
}

// Function To Close the App
function Exit()
{
    window.close()
    eel.Exit()
    
}

//function to clear full output
function ClearFullOutputTextBox()
{
    $("#FullOutputTextArea").val('')
}

//function to clear final output 
function ClearFinalOutputTextBox()
{
    $("textarea#FinalOutputTextArea").val('')
}

//Function to print final song
function PrintFinalOutput(Song)
{
    ClearFinalOutputTextBox()
    console.log("INIDE PRINT FIBAL SONG")
    Song.forEach(function(value)
    {   
        console.log(value)
        value.forEach(function(verse)
        {
            console.log(verse)
            $("textarea#FinalOutputTextArea").val( $("textarea#FinalOutputTextArea").val()+verse)
        })
        $("textarea#FinalOutputTextArea").val( $("textarea#FinalOutputTextArea").val()+"\n")
    })

}
//Function to print full song preview
function PrintFullSong(Song)
{   
    ClearFullOutputTextBox()
    ClearFinalOutputTextBox()
    //Iterater through full song
    console.log("INIDE PRINT FULL SONG")
    Song.forEach(function(value)
    {
        console.log(value)
        //iterate thorugh each verse
        value.forEach(function(verses)
        {
            if(verses.length > 0)
            {
                //keep appending verses
                $("#FullOutputTextArea").val($("#FullOutputTextArea").val()+verses); 
            }      
        })
         //add newline
        $("#FullOutputTextArea").val($("#FullOutputTextArea").val()+"\n");
    })
}
//Function for Autofill
function AutoFill()
{
    var hindi_song_number = document.getElementById("SongNumberHindi").value;
    var telugu_song_number = document.getElementById("SongNumberTelugu").value;

    //FIND TELUGU SONG IF HINDI SONG IS PRESENT
    if (hindi_song_number.length > 0)
    {
        response = eel.AutoFillHindiSongNumber(hindi_song_number)(function(TeluguSongNumber)
        {
            console.log(TeluguSongNumber)
            $("#SongNumberTelugu").val(TeluguSongNumber)
        })
       
    }
    
    else if (telugu_song_number.length > 0)
    {
       response = eel.AutoFillTeluguSongNumber(telugu_song_number)(function(HindiSongNumber)
        {
            $("#SongNumberHindi").val(HindiSongNumber)
        })
       console.log(response)
    }
}
//Function to submit song
function SubmitSongNumber()
{
    song_numbers=[]
    var tamil_song_number = document.getElementById("SongNumberTamil").value;
    var telugu_song_number = document.getElementById("SongNumberTelugu").value;
    var hindi_song_number = document.getElementById("SongNumberHindi").value;

    console.log(tamil_song_number.trim())
    console.log(telugu_song_number.trim())
    console.log(hindi_song_number.trim())

    if (tamil_song_number.length > 0)
    {
        song_numbers.push("TA:"+tamil_song_number)
    }
    if (telugu_song_number.length > 0)
    {
        song_numbers.push("TE:"+telugu_song_number)
    }
    if (hindi_song_number.length > 0)
    {
        song_numbers.push("HE:"+hindi_song_number)
    }

    eel.Search_Song(song_numbers)(function(ret){
        console.log(ret)
        
        let response = ret
        if (response === "No_Song_Error")
        {
            $('#no-song-entered-error-modal').modal('show'); 
        }
        if (response === "Out_Of_Range_Error")
        {
            $('#out-of-range-error-modal').modal('show'); 
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
    
    //calling python function to get the stanzas
    eel.GetVersesToBePrinted(stanzas)(function(value)
    {
        console.log(value)
       
        
            PrintFinalOutput(value)
        
       
    })
}