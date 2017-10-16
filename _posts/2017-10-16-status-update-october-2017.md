---
layout: post
title: "Status update, October 2017."
date: 2017-10-16
---

TapeSync is currently in alpha (as in before beta) being tested by a
handful of users here in Stockholm. The current feature set is very
basic and I want to add a couple of features and some polish before
inviting beta users.


Last week TapeSync was mentioned on the Public Radio NYC listserv and
a bunch of people signed up to the TapeSync email list. A hearty welcome
to all of you and thanks to Ana Adlerstein for the mention!

**Where is TapeSync at right now**


Today TapeSync is a very basic call recording application that will
let you capture phone calls from your phone to any other phone. It's
implemented as a web app that you can use from your computer or
phone. You enter the number you want to call in the web app. The
TapeSync server then places a call to your phone and when you've
picked up the server connects you to the interviewee (who will see
your caller id on their display). After the call, a wav recording is
available for download from within the web app. The audio quality is
comparable to what you'd get by plugging a landline into a
telephone hybrid.


**What's next**

I've been working on the problem that TapeSync solves since early 
2015 but the app that is live now I threw together in a
couple days before summer because my friends
at [Soundtelling](http://soundtelling.com/en/) needed something in a
hurry.

Before I move on to my pool of beta testers (you folks) I need to remodel
the back-end architecture to be a bit more solid and add the following
user-facing features:

  1. Separate tracks for reporter and interviewee.

  2. Reporters end is recorded locally instead of on the telephony
     server. So if you're in a soundproofed studio using a laptop and
     an external microphone your track on the recording will reflect
     that. I hope to be able to do this within the web app approach
     but I might have to move to an app that you download and install
     on your computer.

  3. Automatic transcriptions. Each call recording will be
     automatically transcribed. This will let you search within your
     recordings and will also save you time when logging tape. Automatic
     transcriptions aren't a 100% correct and probably never will be, but
     it's a whole lot better than nothing.

I hope to have this out to beta users in a few months.

**Further down the line**

For later releases I'll be implementing these features:

  1. Recording interviewees in higher definition. Through the TapeSync
     app the reporter can send a call invitation SMS to the
     interviewee. The SMS includes a click-to-call link. When the
     interviewee clicks it they are connected to the reporter via a browser
     call that allows for higher audio quality than regular phone
     calls. The audio quality will hopefully be comparable to what you
     get with the iPhone Voice memo app. The nice thing about this
     approach is that you get good  audio without requiring the
     interviewee to install a special call recording app. If I can't
     get good enough audio quality with this approach I might be forced to
     go the app route anyway.

  2. Synced notes. When calling from a computer the reporter can make
     notes during the call. These notes are time synced with the audio
     so that it's easy to jump back to a specific point in the
     call. Think of this a complement to the automatic transcriptions.

  3. Simple snippets editor. Allow reporters to select snippets to
     download from a wav. This works in conjunction with the auto
     transcription and synced notes. Select a piece of text and get
     the corresponding wav.

**Pricing**

TapeSync is a paid service. There will not be a free version, not even
during the beta. I have to pay third-party providers to make the calls
so operating a free version would quickly bankrupt me. Same goes for
an all-you-can-eat option. The model I've settled on prepaid
calling. You load up your account with credits and can make call
recordings until you run out of credits.

The current price is 0.25 USD/minute and I hope to be able to
stay at that price point even after adding the features mentioned above.

**Your input**

From day one TapeSync has been developed in close collaboration with
documentary radio producers. I've made countless interviews with
producers in Stockholm about their current workflows and their
needs. If you have features you want to see please tell me. If there's
stuff on the roadmap that you think is a total waste of time I'm
equally eager to hear about that. The best way to get in touch with me
is through [oivvio@tapesync.com](mailto:oivvio@tapesync.com).

Stay tuned!


[assets]: /assets/2017/10/16/status-update-october-2017
