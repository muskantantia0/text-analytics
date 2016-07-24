reviews <-reviewamazondata
str(reviews)
review_text <- paste(reviewamazondata$reviewText, collapse=" ")
review_text
review_source <- VectorSource(review_text)
review_source
corpus <- Corpus(review_source)
corpus <- tm_map(corpus, content_transformer(tolower))
corpus
corpus <- tm_map(corpus, stripWhitespace)
corpus
corpus <- tm_map(corpus, removeWords, stopwords("english"))
dtm <- DocumentTermMatrix(corpus)
inspect(dtm)
tdm <- TermDocumentMatrix(corpus)   
tdm
dtm2 <- as.matrix(dtm)
dim(dtm2)
write.csv(dtm2, file="dtm1.csv")
frequency <- colSums(dtm2)                  
frequency <- sort(frequency, decreasing=TRUE)
frequency
head(frequency)
library(wordcloud)
words <- names(frequency)
words
png(height=1600, width=1600, pointsize=15, file="wordcloud.png")
wordcloud(words,scale=c(2,0.2))


