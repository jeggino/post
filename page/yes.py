import streamlit as st

text = """
Finally, I have a bit of time to write something instead of just posting photos...

...Let’s start from far, far away…🤓

In ecology, the relationships between different species are named symbiosis. There are three main types of symbiosis: parasitism, mutualism, and commensalism, and they are based on who gains or loses in the interaction. In simple terms, in parasitism, one species loses while the other gains; in mutualism, both species gain; and in commensalism, one species gains and the other neither gains nor loses. Or better saying, commensalism is "an interaction in which one species gains while the other is not severely damaged or benefited."
Humans, as a species within the ecosystem, also interact with other species in these ways - often as a parasite, sometimes as a commensal, and almost never as a mutualist...just to make it clear.

Among the species that have a commensal relationship with humans are those that live and nest in human settlements. In the Netherlands, there are various species of bats and birds that occupy these places. From my experiences, Dutch people tend to be very positive about the presence of these animals. I have met many people who feel joyful about having a bat maternity roost or a swift nest in their roofs, getting a sense of "happiness and serenity" from them. If additionally you consider the ecological services they provide, "contributing to a more complex and stable urban ecosystem", it is possible to say that these species have a more mutualistic relationship with humans, that just stay in your place without paying the rent...jajaj.
Unfortunately, having these species in your home is not always 'rose e fiori'. They can bring many problems, for example when you need to do some renovation in your roof. For this reason, unfortunately, some people have begun to consider them more like pests.

In some ways, the Netherlands can be considered a virtuous country. Despite the rising pressure from some politicians, there is still an effort to balance both sides.
In the last decade, many projects have been funded to monitor the distribution of these species in urban areas and to mitigate the impacts on their populations. However, these projects often require huge investments, and, for this reason, many ecologists are working to make the conservation of these species sustainable and feasible in the long term. One approach is to create species distribution models based on factors that positively or negatively affect the presence of these species. These models are particularly useful for optimizing survey efforts. For bats, for example, the age and energy label of buildings is often used to predict the likelihood of finding a maternity roost because older buildings with lower energy labels typically have more places for bats to hide.

Now, the main reason for this post… 😅😅!

The video shows a quite big maternity roost (75 specimens) of Pipistrellus pipistrellus that I found and counted this season. While counting, I took a better look at the building and found that it seemed quite new and neat. I got curious and I checked its construction year and energy label, and I found that it was quite new and received an energy label (A) in 2019. In this case, trusting only in the model would have disastrous consequences for this beautiful colony, as the building would have been considered "not suitable" for bats.

and now it's time for my naive hypothesis…☺️☺️

As a colleague of mine let me notice, the colony emerged from the "hottest" area of the roof, as highlighted by heat camera footage.
So..
Wouldn't it be helpful to implement heat night vision cameras, maybe installed on cars or drones, to map the presence of these "hotter" spots in big areas?

Thanks for reading! I know this could be boring ✌️✌️...your comments are very appreciated.
"""

video = """
https://anydhrpvfenefacuoarv.supabase.co/storage/v1/object/sign/video/WhatsApp%20Video%202025-11-28%20at%2018.47.05_1ca38e99.mp4?token=eyJraWQiOiJzdG9yYWdlLXVybC1zaWduaW5nLWtleV81ODFiOTg5ZS1mM2ZkLTQ3NTktYTAxMS1iNmU4ZmNjMmJmNDkiLCJhbGciOiJIUzI1NiJ9.eyJ1cmwiOiJ2aWRlby9XaGF0c0FwcCBWaWRlbyAyMDI1LTExLTI4IGF0IDE4LjQ3LjA1XzFjYTM4ZTk5Lm1wNCIsImlhdCI6MTc2NDg3MDMwNSwiZXhwIjoxNzk2NDA2MzA1fQ.VAZWRNr1307MbmPYWBEb0lFcp71Xd19M6PSWsqFqiWs
"""

col1, col2 = st.columns([2,1])

col1.markdown(text)

col2.video(video)

