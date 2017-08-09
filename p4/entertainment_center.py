#here we are importing our fresh_tomatoes file nad media file tso as to access the classes inside it
import fresh_tomatoes
import media
Thor = media.Movie("Thor Ragnarok",
                   "Imprisoned on the other side of the universe, the mighty Thor finds himself in a deadly gladiatorial contest that pits him against the Hulk, his former ally and fellow Avenger",
                   "https://www.quirkybyte.com/wp-content/uploads/2017/01/NEOe3FBKEIX3SQ_2_b.jpg",
                   "https://www.youtube.com/watch?v=ue80QwXMRHg",
                   )
#here we are parsing arguments or say passing the information to Movie class of media file o.e the function __init__ we made 
IronMan = media.Movie("IronMan",
                   "After being held captive in an Afghan cave, billionaire engineer Tony Stark creates a unique weaponized suit of armor to fight evil",
                   "http://www.imdb.com/title/tt0371746/mediaviewer/rm1544850432",
                   "http://www.imdb.com/title/tt0371746/videoplayer/vi447873305?ref_=tt_ov_vi",
                    )
captain_america = media.Movie("Captain America:Civil War",
                   "Political interference in the Avengers' activities causes a rift between former allies Captain America and Iron Man.The new status quo deeply divides members of the team. Captain America believes superheroes should remain free to defend humanity without government interference. Iron Man sharply disagrees and supports oversight.As the debate escalates into an all-out feud, Black Widow (Scarlett Johansson) and Hawkeye (Jeremy Renner) must pick a side.",
                   "http://t3.gstatic.com/images?q=tbn:ANd9GcTz1xU3qYlGXViIS51HIQh71D339ceW2nlWnb8zzSaJAL0newVj",
                   "http://www.imdb.com/title/tt3498820/videoplayer/vi174044441?ref_=tt_ov_vi",
                   )
Deadpool = media.Movie("Deadpool",
                   "Wade Wilson is a former Special Forces operative who now works as a mercenary. His world comes crashing down when evil scientist Ajax (Ed Skrein) tortures, disfigures and transforms him into Deadpool. The rogue experiment leaves Deadpool with accelerated healing powers and a twisted sense of humor. With help from mutant allies Colossus and Negasonic Teenage Warhead (Brianna Hildebrand), Deadpool uses his new skills to hunt down the man who nearly destroyed his life.",
                   "http://t2.gstatic.com/images?q=tbn:ANd9GcTvrIHJfasS6poy34esN1O5hZonXaiqfEZb4WbnbAa9qJCIL8_9",
                   "https://www.youtube.com/watch?v=FyKWUTwSYAs",
                   )
Avengers = media.Movie("Avenger-Infinity-War",
                   "Avengers: Infinity War is an upcoming American superhero film based on the Marvel Comics superhero team the Avengers",
                   "https://static1.squarespace.com/static/53323bb4e4b0cebc6a28ffa2/t/58faebd3c534a56ca615ea58/1492839386320/",
                   "https://www.youtube.com/watch?v=1_OcO3nbDMI"
                   )
BlackPanther = media.Movie("BlackPanther",
                   "T'Challa, after the death of his father, the King of Wakanda, returns home to the isolated, technologically advanced African nation to succeed to the throne and take his rightful place as king.",
                   "http://vignette3.wikia.nocookie.net/marveldatabase/images/e/ee/Original_Sin_Vol_1_2_Dell%27Otto_Variant_Textless.jpg/revision/latest?cb=20140220070551",
                   "https://www.youtube.com/watch?v=Q7Q3WbF__NY"
                   )
movies = [Ironman,captain_america,Deadpool,Avengers,BlackPanther]
fresh_tomatoes.open_movies_page(movies)
