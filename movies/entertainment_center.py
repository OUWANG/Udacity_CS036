import fresh_tomatoes
import media

toy_story_3 = media.Movie("Toy Story 3",
                        "A story of a boy and his toys come to life",
                        "https://upload.wikimedia.org/wikipedia/en/6/69/Toy_Story_3_poster.jpg",
                        "https://www.youtube.com/watch?v=JcpWXaA2qeg")
avatar = media.Movie("Avatar",
                        "A marine on an alien planet",
                        "https://upload.wikimedia.org/wikipedia/en/b/b0/Avatar-Teaser-Poster.jpg",
                        "https://www.youtube.com/watch?v=5PSNL1qE6VY")
crazy_rich_asians = media.Movie("Crazy Rich Asians",
                              "A love story of a girl to be marrying into the rich asian family",
                              "https://upload.wikimedia.org/wikipedia/en/b/ba/Crazy_Rich_Asians_poster.png",
                              "https://www.youtube.com/watch?v=ZQ-YX-5bAs0")
mission_impossible_fallout = media.Movie("Mission: Impossbile - Fallout",
                                         "Doing all kinds of cool shit impossible",
                                         "https://upload.wikimedia.org/wikipedia/en/f/ff/MI_%E2%80%93_Fallout.jpg",
                                         "https://www.youtube.com/watch?v=XiHiW4N7-bo")
ratatouille = media.Movie("Ratatouille",
                          "Rat cooking French cuisine",
                          "https://upload.wikimedia.org/wikipedia/en/5/50/RatatouillePoster.jpg",
                          "https://www.youtube.com/watch?v=c3sBBRxDAqk")
sausage_party = media.Movie("Sausage Party",
                            "Food coming to life",
                            "https://upload.wikimedia.org/wikipedia/en/e/e4/Sausage_Party.png",
                            "https://www.youtube.com/watch?v=9VoNgLnjzVg")

movies = [toy_story_3, avatar, crazy_rich_asians, mission_impossible_fallout, ratatouille, sausage_party]

fresh_tomatoes.open_movies_page(movies)
