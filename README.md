# <p align="center">LoreBubbl</p>
<p align="center">
  <img src="assets/app_icon.png" alt="LoreBubbl Logo" width="300"/>
</p>

LoreBubbl uses AI to help people with short attention spans get contextual awareness while reading books. This was built by Aditya, Dheeraj, Sahil, and Shravan during the Tidal Hackathon at TAMU. This repository consists of the backend aspect of the project, which includes a custom RAG pipeline, along with entity context retrieval, and the LLM connection. LoreBubbl is built using Flutter, keeping cross-platform support in mind.

- The frontend UI can be accessed from [this repository][1].

- Demo Link: https://www.youtube.com/watch?v=yN_OHNdW5B8 

## Inspiration
Some of my friends have difficulties remembering things while they read books. They tend to read the same page again and again to try and remember the context of the situation or an entity.

So we built *LoreBubbl*, an AI-powered reader app that provides contextual awareness and information about a character, item, place, entity, or situation in the book.

## What it does
LoreBubbl uses AI to retrieve the context of a situation or summarize a segment of text (a line, paragraph, page, or chapter).

The user can highlight the text and ask for the context of it. It uses a customized *C-RAG* (Context - Retrieval Augmented Generation) along with prompt engineering to talk to an LLM and create a perfect overall context for the highlighted text, based on the scenario that's happening, and entity context that was retrieved from the book using an LLM.

## How we built it
We used *Flutter* for the front-end, keeping cross-platform support in mind. The backend, which was written in *Python, contains the RAG pipeline, LLM connection, and the APIs required to talk to the front-end, using **Flask*.

We used *SentenceTransformer* (paraphrase-MiniLM) to handle the creation of the embedding matrix. *AWS Bedrock* was used with *LLama3.1 70b* model for entity context and contextual awareness retrieval.

## Challenges we ran into
We didn't have any experience with mobile app development with Flutter, so that was slightly a blocker. When we were building the RAG and LLM pipeline, we faced issues with knowledge graph generation, which we fixed after spending a few hours learning more about KRAGs in depth.

*Integrating Flutter app to the backend AI* code was another challenge since we had no idea how to.

*LLMs have hallucinations*, which can affect the accuracy of the platform. This was a challenge, as we did not know how to fix this in the beginning.

## Accomplishments that we're proud of
To solve the hallucinations, we created an *entity context retrieval* using LLMs, to help the RAG process argument more knowledge to the LLM while performing context retrieval. That was a brilliant idea to solve this issue.

*Flutter was a new domain for all of us*, and putting effort into learning a new language in under 4 hrs is something all of us are proud of.

*We created a new kind of RAG* from scratch, with entity context awareness, which is very sparse in the market.

[Llama LLM backend](https://github.com/reddheeraj/Text-Referencer)

## What we learned
We didn't have any experience with mobile app development with Flutter, so that was a new learning experience.

Building an entirely new RAG for this specific use case was a first for all of us, and we learned a lot while building the project.

## What's next for LoreBubbl
We plan to extend its use case to academia, where textbooks and research papers can come into the picture, for advanced learning experience.

One feature that we are willing to work on is a way for the user to chat with the book that they are reading. The user could directly highlight text and ask questions about a particular aspect.

We also have ideas to add context retrieval from the web, like forums and discussion pages for highly constricted opinions about a situation/scenario/entity from the book.


[1]: https://github.com/pseudou/eReader-app


<!-- A quick POC that I built. you can highlight a line or bunch of lines in an ebook online and you will be able to see similar text/context on a pop-up, from the previous pages of the book. -->

