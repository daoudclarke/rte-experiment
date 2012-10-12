Experiments in Recognising Textual Entailment
=============================================

This repository contains python code for experiments relating to
RTE. At the moment, the main thing of interest here is the Guardian
Headlines Entailment Training Dataset.

What is Textual Entailment?
---------------------------

Recognising Textual Entailment (RTE) is the task of determining, given
two sentences whether the first (called the "text") entails or implies
the second (called the "hypothesis"). In this task, the term
"entailment" is generally fairly loosely defined, and datasets are
normally built by asking human subjects whether they consider
entailment to hold.

RTE as a field of study really kicked off with the [Recognising
Textual Entailment
Challenge](http://pascallin.ecs.soton.ac.uk/Challenges/RTE/).

Why Textual Entailment?
-----------------------

Textual Entailment is a generalisation of many tasks in natural
language processing. If you have a system that is good at recognising
textual entailment, it should be easier to build good systems for
information retrieval, question answering, paraphrase recognition,
information extraction and summarisation.

The need for automatically constructed datasets
-----------------------------------------------

Because of the expense of manually constructing entailment datasets,
they are normally fairly small, which means machine learning
approaches to the task perform sub-optimally.

As  [Hickl et al.](http://u.cs.biu.ac.il/~nlp/RTE2/Proceedings/14.pdf)
showed, automatically constructed datasets can improve the performance
of systems using machine learning by up to ten percent.

The Guardian Headlines Entailment Training Dataset
--------------------------------------------------

The dataset consists of around 32,000 pairs of sentences (16,233 for
which entailment does hold and 16,249 for which it doesn't)
automatically extracted from The Guardian newspaper using their
API. We follow a similar methodology to [Hickl et
al.](http://u.cs.biu.ac.il/~nlp/RTE2/Proceedings/14.pdf): we treat
headlines as being entailed by the first sentence, and adjacent
sentences in the remainder of the text as non-entailing.

Each pair must pass a number of criteria (arrived at in a fairly
ad-hoc manner):
 * The pair must share a named entity (or part of a named entity) in
   common (as required by Hickl et al.)
 * Each sentence in the pair must not be too short or long
 * Each sentence must not contain too many new line characters
 * Each sentence must contain an even number of quotation marks

The source of the data is 78,696 Guardian articles from 1st January
2004 onwards obtained through the Guardian API.

No analysis has yet been performed on the dataset, so use it at your
own risk! The intention is eventually to manually analyse a sample of
the data.

The data is in XML format and is the same as the RTE-1 dataset:

    <pair id="1" value="TRUE">
     <t>
      Italian authorities yesterday blocked mail from Bologna addressed
      to EU institutions as they tried to end a letter-bomb assault that
      has been aimed at European targets.
     </t>
     <h>
      Mail block to catch EU book bombs
     </h>
    </pair>



License
-------

Permission is hereby granted, free of charge, to any person obtaining
a copy of this software and associated documentation files (the
"Software"), to deal in the Software without restriction, including
without limitation the rights to use, copy, modify, merge, publish,
distribute, sublicense, and/or sell copies of the Software, and to
permit persons to whom the Software is furnished to do so, subject to
the following conditions:

The above copyright notice and this permission notice shall be
included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND
NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE
LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION
OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION
WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
