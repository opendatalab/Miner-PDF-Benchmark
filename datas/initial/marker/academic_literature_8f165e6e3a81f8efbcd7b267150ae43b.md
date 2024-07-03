# Svdd Challenge 2024: A Singing Voice Deepfake Detection Challenge Evaluation Plan

You Zhang∗1, Yongyi Zang∗1, Jiatong Shi∗2, Ryuichi Yamamoto∗3, Jionghao Han2, Yuxun Tang4, Tomoki Toda3*, Zhiyao Duan*1 targets both controlled and in-the-wild settings, aiming to distinguish bonafide and AI-generated singing voice recordings.

## 2. Challenge Objectives

1University of Rochester, Rochester, NY, USA 2Carnegie Mellon University, Pittsburgh, PA, USA
3Nagoya University, Nagoya, Japan 4Renmin University of China, Beijing, China svddchallenge@gmail.com https://challenge.singfake.org

## Abstract

The rapid advancement of AI-generated singing voices, which now closely mimic natural human singing and align seamlessly with musical scores, has led to heightened concerns for artists and the music industry. Unlike spoken voice, singing voice presents unique challenges due to its musical nature and the presence of strong background music, making singing voice deepfake detection (SVDD) a specialized field requiring focused attention. To promote SVDD research, we recently proposed the "SVDD Challenge," the very first research challenge focusing on SVDD for lab-controlled and in-the-wild bonafide and deepfake singing voice recordings. The challenge will be held in conjunction with the 2024 IEEE Spoken Language Technology Workshop (SLT 2024). Index Terms: singing voice deepfake detection, anti-spoofing

## 1. Introduction

The development of advanced singing voice synthesis techniques has led to a significant milestone in AI-generated content, where singing voices sound remarkably natural and align seamlessly with music scores. These synthesized voices can now emulate the vocal characteristics of any singer with minimal training data. While this technological advancement is impressive, it has sparked widespread concerns among artists, record labels, and publishing houses [1]. The potential for unauthorized synthetic reproductions that mimic well-known singers poses a real threat to original artists' commercial value and intellectual property rights, igniting urgent calls for efficient and accurate methods to detect these deepfake singing voices.

In response to these concerns, our prior research [2] has laid the groundwork for the emerging field of SVDD. We introduced the SingFake dataset, a comprehensive collection of authentic and deepfake song clips featuring a variety of languages and singers. Our findings revealed a critical insight: conventional speech countermeasure (CM) systems, when trained on standard speech, experience significant performance degradation when tested on singing voices. Conversely, retraining these systems specifically on singing voice data resulted in notable improvements. Our prior evaluations also highlighted several challenges, including dealing with unseen singers, various communication codecs, diverse languages and musical contexts, and interference from accompaniment tracks. This highlights the distinct nature of singing voice deepfakes and the necessity for specialized SVDD systems.

To advance the field of singing voice deepfake detection, we introduce the SVDD challenge, the inaugural research initiative specifically dedicated to exploring SVDD. This challenge
* These authors contributed equally. Version 1.2. Updated: May 9, 2024. Correspondence addressed to you.zhang@rochester.edu The SVDD challenge aims to bring together the academic and industrial communities to develop innovative and effective techniques for detecting deepfake singing voices. We hope this challenge will advance our understanding of the specific traits of singing voice deepfakes and contribute to the broader field of multimedia deepfake detection.

## 3. Challenge Setups

In the context of singing voice deepfakes, a common practice is to present these artificial creations alongside background music, as observed in our SingFake [2] project. This approach, while practical for simulating authentic song presentations, introduces a significant challenge: the separation of vocals from music may create artifacts that can obscure the differences between bonafide and deepfake vocals. To investigate this issue thoroughly, the SVDD challenge is structured into two distinct tracks: the *controlled* and the *in-the-wild* settings. The WildSVDD track follows the same approach as our SingFake project [2], dealing with deepfakes as they typically appear in online media, complete with background music. In contrast, the CtrSVDD track exclusively uses clean, unaccompanied vocals provided by our data contributors, thereby minimizing the interference of voice separation algorithms. This two-track approach lets participants tackle the challenges of identifying deepfake singing voices under different and realistic conditions. This section describes our dataset curation for setting up the two tracks.

## 3.1. Ctrsvdd: Controlled Singing Voice Deepfake Detection

For the CtrSVDD track, we first source bonafide datasets from existing open-source singing recordings. These include Mandarin singing datasets: Opencpop [3], M4Singer [4], Kising [5],
Official ACE-Studio release, and Japanese singing datasets:
Ofuton-P1, Oniku Kurumi2, Kiritan [6], and JVS-MuSiC [7].

We perform segmentation to divide the songs into vocal clips.

We then generate deepfake singing vocals with 14 existing singing voice synthesis (SVS) and singing voice conversion (SVC) systems from these bonafide vocals. For SVS,
we employ ESPnet-Muskits [8], NNSVS [9], DiffSinger [10],
and ACESinger3. For SVC, we apply the NU-SVC [11] and

![1_image_0.png](1_image_0.png)

Singer Seen Seen Unseen Unseen Unseen variants of So-VITS-SVC4. When dividing the generated deepfakes into train, development, and evaluation splits, we follow the approach used in the speech deepfake detection benchmark ASVspoof2019. We employ the same set of deepfake generation algorithms (A01-A08) for both the training and development sets, while using a different set of deepfakes (A09-A14)
for the evaluation partition. We plan to release more details on deepfake systems in early June.

Codec Seen Seen Seen Unseen Unseen Context Seen Seen Seen Seen **Unseen**

## 3.2.Wildsvdd: In-The-Wild Singing Voice Deepfake Detection

We have continued to gather data annotations from social media platforms following a method similar to the SingFake project [2]. The WildSVDD dataset has been expanded to approximately double the original size of SingFake, now featuring 97 singers with 3223 songs. The annotators, who are familiar with the singers they cover, manually verified the user-specified labels during the annotation process to ensure accuracy, especially in cases where the singer(s) did not actually perform certain songs. We cross-check the annotations against song titles and descriptions, and manually review any discrepancies for further verification. We have verified the accessibility of all URLs in the dataset as of March 28th and removed any that were inaccessible. The WildSVDD dataset now includes Korean singers, making Korean the third most represented language in the dataset. To help track changes between the SingFake and WildSVDD datasets, we have added a "SingFake Set" column that indicates the original partition of an annotation in the SingFake dataset. Annotations that lack a value in this column are new additions to the WildSVDD dataset.

Due to potential copyright issues, we are currently only releasing the annotations. Consequently, participants might acquire slightly different media files that correspond to the same annotations, depending on the specifics of their download process. Due to this variability, self-reported metrics from participants can, at best, be used as a rough reference and cannot be directly used to compare systems. As such, we encourage participants to report the success rate of URL downloads per partition and, if possible, the actual files used for training and testing. This transparency will allow researchers to make fairer comparisons. Additionally, participants are encouraged to describe their model designs clearly and open-source their model implementations to facilitate the reproduction of results with the WildSVDD dataset.

SVDD Challenge 2024 @ IEEE SLT Workshop **References**
[1] Simon Rouard, Francisco Massa, and Alexandre Defossez, ´ "Hybrid transformers for music source separation," in Proc. IEEE International Conference on Acoustics, Speech and Signal Processing (ICASSP), 2023. 

[2] Jee-weon Jung, Hee-Soo Heo, Hemlata Tak, Hye-jin Shim, Joon Son Chung, Bong-Jin Lee, Ha-Jin Yu, and Nicholas Evans, "AASIST: Audio anti-spoo ng using integrated spectro-temporal graph attention networks," in Proc. IEEE International Conference on Acoustics, Speech and Signal Processing (ICASSP), 2022, pp. 6367–6371. 

[3] You Zhang, Fei Jiang, and Zhiyao Duan, "One-class learning towards synthetic voice spoo

## 4. Evaluation Metrics

We use Equal Error Rate (EER) to evaluate the SVDD system performance. We expect each SVDD system submitted by par-4https://github.com/HANJionghao/so-vits-svc2 Table 1: Summary of the training and development partition of the CtrSVDD dataset.

| Partition   | # Speakers   | Bonafide     | Deepfake   |         |
|-------------|--------------|--------------|------------|---------|
| # Utts      | # Utts       | Attack Types |            |         |
| Train       | 59           | 12,169       | 72,235     | A01∼A08 |
| Dev         | 55           | 6,547        | 37,078     | A01∼A08 |

ticipants to generate a score TXT file, which contains scores for every segmented clip. These scores reflect the system's confidence in whether the vocal or song clip originates from a bona fide singer or resembles a real singer. A higher score indicates greater confidence that the clip is from a real singer. In practical usage, people may set a threshold to determine the binary output of bonafide or deepfake. With the threshold higher, the false acceptance rate will become lower, and the false rejection rate will become higher. The EER is achieved when these two are equal, as illustrated in Figure 1. The EER is more suitable to evaluate the system's performance than accuracy since it is not dependent on the threshold. The lower the EER, the better the system distinguishes bonafide and deepfake singing voices.

## 5. Protocols 5.1. Ctrsvdd Track

The CtrSVDD data is released under a CC-BY-NC-ND 4.0 license, aligned with the sourcing corpora. We have released the training and development set on Zenodo5and other relevant scripts on GitHub6. Please be aware that the training and development set available on Zenodo is incomplete because of licensing issues. To fully generate the dataset, first download all the remaining bonafide datasets on your own by agreeing to their terms and conditions, and then follow the detailed instructions provided in the GitHub repository. Participants can refer to the statistics in Table 1 as a guide to verify the completion of their downloads and generation.

For evaluation, we have released the test set on Zenodo7 with undisclosed labels at a later date and ask teams to score each song vocal clip. There are, in total, 48 speakers with 92,769 clips. Using the submitted scores, we will calculate and rank participant systems using EER. For submission guidelines, please refer to Section 9.

## 5.2. Wildsvdd Track

The WildSVDD track data has been released on Zenodo8under a CC-BY 4.0 license. We supply the training and test partitions, allowing participants the flexibility to carve out a validation set from the training data for model development. We provide labels of SingFake [2] partitions for annotations that appeared in the SingFake dataset for easy comparison with previous systems. The test set is divided into parts A and B, with part B
considered more challenging due to its inclusion of unseen musical contexts as T04 in SingFake [2].

We recommend that participants further segment the songs into clips using our tool available in the SingFake GitHub repos-5https://zenodo.org/records/10467648 6https://github.com/SVDDChallenge/CtrSVDD_
Utils 7https://zenodo.org/records/10742049 8https://zenodo.org/records/10893604 ng detection," IEEE Signal Processing Letters, vol. 28, pp. 937–941, 2021. 

[4] Hemlata Tak, Massimiliano Todisco, Xin Wang, Jee weon Jung, Junichi Yamagishi, and Nicholas Evans, "Automatic speaker verification spoofing and deepfake detection using wav2vec 2.0 and data augmentation," in Proc. The Speaker and Language Recognition Workshop (Odyssey), 2022, pp. 112–119.

itory9. Evaluations should be conducted at the segment level rather than at the song level. We will adopt the self-reported EER and will not accurately rank the results. We encourage the participants to submit the score files listing the URLs, segment index, and the corresponding scores output from their systems.

## 6. Rules For Developing Svdd Systems

Participants are welcome to use any publicly available datasets for training in addition to the CtrSVDD we provide, but of course, exclude any datasets used in our test set. Specifically, for the CtrSVDD track, participants must NOT use M4Singer, KiSing, any open-sourced deepfake models based on M4Singer and/or KiSing, or the commercial software ACE Studio10.

We refer the participants to the list of available datasets at the end of this section. However, participants must document any additional data sources used in their system descriptions. If there are any public data sources not listed but you would like to use for training, please inform the organizers so that we can share this information among participants. We will maintain and update the list of data sources until the registration deadline.

If the participants are willing to generate new training data from our released data and other public datasets for the CtrSVDD track, they can request permission to use such data under the condition that this new dataset will be published to other participants. We have set a deadline for this request.

Please refer to Section 11 for details.

The use of publicly available pre-trained models is also permitted. Participants should specify the exact version of the pretrained models used and provide a link to the pre-trained embedding used in the system description.

Any private data or private pre-trained models are strictly forbidden to use.

Participants should not add additional annotations to the WildSVDD track for training. Please contact the organizers if you are interested in contributing more annotations for future research.

Below we provide a list of known data sources as a reference. This list applies to both CtrSVDD and WildSVDD tracks.

- Speech Anti-Spoofing datasets: ASVspoof 2019 [12],
ASVspoof 2021 [13], In-the-wild [14], WaveFake [15]
- Speech Synthesis datasets: LJSpeech [16], VCTK [17], LibriTTS [18], Hi-Fi TTS [19], LibriSpeech [20], CommonVoice [21], LibriLight [22],
- Singing Voice Synthesis datasets: NUS-48E [23],
OpenSinger [24], CSD [25], VocalSet [26], Ameboshi ciphyer utagoe db11, itako singing12, JSUT13, Namine ritsu utagoe db14, Natsume15, NIT song07016, No7 singing17, PJS [27], PopCS [10], Dsing [28],
SingStyle111 [29]
- Audio-Visual Singing Voice datasets: URSing [30], A cappella [31]

![2_image_0.png](2_image_0.png)

- Singing Voice DeepFake Detection datasets: SingFake [2],
FSD [32].

## 7. Baselines

We have developed two baseline systems for the challenge: one that uses raw waveforms and another that employs linear frequency cepstral coefficients (LFCCs) as front-end features. The architecture of the baseline systems is shown in Figure 2.

The raw waveform system is based on the AASIST [33],
with several modifications: 1) We reduced the number of output classes from two to one. 2) We adopted binary cross entropy with focal loss for training, setting the focusing parameter (γ)
to 2.0 and the weight for positive examples (α) to 0.25. 3) We omitted stochastic weight averaging. 4) We implemented a cosine annealing learning rate schedule with a maximum of 10 iterations and a minimum learning rate of 1e-6. 5) We used the Adam optimizer, incorporating a weight decay of 1e-9.

The LFCC system used 60 coefficients and 20 filters, with a 512 sample window and 160 sample hop size. The LFCC features pass through several downsampling residual convolution blocks and a linear layer connecting it to the graph attention network backend of [33].

We refer to the LFCC system as B01 and the raw waveform model as B02. For both systems, we conducted training over 100 epochs using a fixed random seed, exclusively on the CtrSVDD training partition. We then selected the checkpoint that achieved the lowest validation EER on the CtrSVDD development partition for evaluation. During training and evaluation, the models processed 4-second random audio segments from each utterance. Details of the implementation are available on the challenge GitHub repository18.

On the CtrSVDD evaluation set, the B01 system achieved an Equal Error Rate (EER) of 11.3697%, while the B02 system recorded a slightly lower EER of 10.3851%. The performance on the validation set across each training epoch is illustrated in 18https://github.com/SVDDChallenge/
CtrSVDD2024_Baseline

![3_image_0.png](3_image_0.png)

Figure 3, where we observed a rapid decline in the validation EER to below 1%, even nearing 0. However, the performance on the evaluation set did not match this, indicating challenges in generalizing the detection of unseen singing voice deepfake generation methods. We hence encourage the participants to explore methods of improving such generalization ability.

For the WildSVDD, we will employ the same baseline systems architecture. While performance results are pending, we anticipate they will align closely with those reported in [2].

## 8. Registration Process Please Use The Following Google Form To Register. Https://Forms.Gle/Fbmeyahovyqzsm927 9. Submission Of Results

We ask the participants to submit the test set scores and system descriptions, which will be published on the challenge website. For reproducible research, we encourage the participants to open-source both the training code and inference code.

We have opened CodaBench19 [34] for CtrSVDD results submission. Each team is allowed a maximum of THREE submissions for the entire duration of the CtrSVDD challenge for official ranking purposes. This limit is in place to ensure fairness and to encourage strategic submissions. It's important to note that CodaBench's daily submission limit is separate; our three-submission limit refers to the total allowable submissions for the challenge.

Additional submissions may be used for comparative analyses in participants' research papers. After using your THREE
allotted submission opportunities, the organizers will help you register for a new CodaBench20 for further submissions. These additional submissions will be considered for research purposes ONLY and will not affect official challenge rankings. We regularly monitor submissions on CodaBench, but if you do not receive access to the new CodaBench within a day after exhausting your challenge submissions, please contact the organizers.

If you wish to use the second CodaBench without participating in the challenge, please inform the organizers to gain access.

19https://www.codabench.org/competitions/2178 20https://www.codabench.org/competitions/3004

## 10. Paper Submission

A special session dedicated to the SVDD challenge will be featured at SLT 202421. Participants in the SVDD challenges may choose to submit papers via the regular submission system, which will go through SLT peer review process.

Additionally, challenge participants have the option to submit papers describing their systems to distinct Challenge Proceedings. The challenge organizers will review these submissions. While accepted system description papers will not be indexed by IEEE, authors will be given the opportunity to showcase their work during a specific session at the workshop, facilitating a focused exchange on advancements in SVDD.

We also plan to make all submitted system descriptions publicly available on the challenge website22, unless participants choose not to and inform us of their decision.

## 11. Important Dates

Timeline of the challenge:
- January 8th, 2024, Release of CtrSVDD training / development data - January 19th, 2024, Release of the baseline system implementation for CtrSVDD
- March 2nd, 2024, CodaBench for challenge submissions open, release of test data and baseline systems for the CtrSVDD track
- March 29th, 2024, Release of WildSVDD dataset URLs
- April 2nd, 2024, Release of evaluation plan version 1.0
- May 7th, 2024, CodaBench for research result submissions open (access upon request)
- June 8th, 2024, SVDD Challenge Registration deadline
- June 8th, 2024, SVDD Challenge additional training dataset permission request deadline
- June 8th, 2024, Organizers post all available training datasets - June 15th, 2024, Results submission deadline (Results &
system description), CodaBench challenge submission close. Results will be publicly available on CodaBench and emailed to participants for official confirmation.

- June 20th, 2024, SLT Paper submission - June 27th, 2024, SLT Paper update - August 30, 2024, SLT Paper notification - December 2nd - 5th, 2024, SVDD special session at SLT
2024

## 12. Acknowledgement

We acknowledge the contributions from ACESinger for supporting our CtrSVDD track and agree to provide participants with access to the singers' bonafide singing data. We also appreciate the support from team Opencpop [3], the WeNet community, and all other bonafide data providers.

We acknowledge Yoav Zimmerman23, Chang-Heon Han
(Hanyang University, Korea), Jing Cheng (University of Rochester, USA), and Mojtaba Heydari (University of Rochester, USA) for their contributions to part of the WildSVDD data annotation.

## 13. References

[1] N. Collins and M. Grierson, "Avoiding an AI-imposed taylor's version of all music history," *arXiv preprint arXiv:2402.14589*,
2024.

[2] Y. Zang, Y. Zhang, M. Heydari, and Z. Duan, "SingFake: Singing voice deepfake detection," in *Proc. IEEE International Conference on Acoustics, Speech and Signal Processing (ICASSP)*, 2024.

[3] Y. Wang, X. Wang, P. Zhu, J. Wu, H. Li, H. Xue, Y. Zhang, L. Xie, and M. Bi, "Opencpop: A high-quality open source chinese popular song corpus for singing voice synthesis," in *Proc. Interspeech*,
2022, pp. 4242–4246.

[4] L. Zhang, R. Li, S. Wang, L. Deng, J. Liu, Y. Ren, J. He, R. Huang, J. Zhu, X. Chen, and Z. Zhao, "M4singer: A multi-style, multi-singer and musical score provided mandarin singing corpus," in *Proc. Neural Information Processing Systems* Datasets and Benchmarks Track, 2022.

[5] J. Shi, Y. Lin, X. Bai, K. Zhang, Y. Wu, Y. Tang, Y. Yu, Q. Jin, and S. Watanabe, "Singing voice data scaling-up: An introduction to ace-opencpop and kising-v2," *arXiv preprint arXiv:2401.17619*,
2024.

[6] I. Ogawa and M. Morise, "Tohoku kiritan singing database: A
singing database for statistical parametric singing synthesis using japanese pop songs," *Acoustical Science and Technology*, vol. 42, no. 3, pp. 140–145, 2021.

[7] H. Tamaru, S. Takamichi, N. Tanji, and H. Saruwatari, "JVSMuSiC: Japanese multispeaker singing-voice corpus," *arXiv* preprint arXiv:2001.07044, 2020.

[8] J. Shi, S. Guo, T. Qian, T. Hayashi, Y. Wu, F. Xu, X. Chang, H. Li, P. Wu, S. Watanabe, and Q. Jin, "Muskits: an end-to-end music processing toolkit for singing voice synthesis," in *Proc. Interspeech*, 2022, pp. 4277–4281.

[9] R. Yamamoto, R. Yoneyama, and T. Toda, "NNSVS: A neural network-based singing voice synthesis toolkit," in *Proc. IEEE International Conference on Acoustics, Speech and Signal Processing (ICASSP)*, 2023, pp. 1–5.

[10] J. Liu, C. Li, Y. Ren, F. Chen, and Z. Zhao, "Diffsinger: Singing voice synthesis via shallow diffusion mechanism," in *Proc. AAAI*
Conference on Artificial Intelligence, vol. 36, no. 10, 2022, pp.

11 020–11 028.

[11] R. Yamamoto, R. Yoneyama, L. P. Violeta, W.-C. Huang, and T. Toda, "A comparative study of voice conversion models with large-scale speech and singing data: The T13 systems for the singing voice conversion challenge 2023," in *Proc. IEEE Automatic Speech Recognition and Understanding Workshop (ASRU)*,
2023, pp. 1–6.

[12] X. Wang, J. Yamagishi, M. Todisco, H. Delgado, A. Nautsch, N. Evans, M. Sahidullah, V. Vestman, T. Kinnunen, K. A. Lee et al., "ASVspoof 2019: A large-scale public database of synthesized, converted and replayed speech," *Computer Speech & Language*, vol. 64, p. 101114, 2020.

[13] X. Liu, X. Wang, M. Sahidullah, J. Patino, H. Delgado, T. Kinnunen, M. Todisco, J. Yamagishi, N. Evans, A. Nautsch *et al.*,
"ASVspoof 2021: Towards spoofed and deepfake speech detection in the wild," *IEEE/ACM Transactions on Audio, Speech, and* Language Processing, 2023.

[14] N. Muller, P. Czempin, F. Diekmann, A. Froghyar, and ¨
K. Bottinger, "Does Audio Deepfake Detection Generalize?" in ¨
Proc. Interspeech, 2022, pp. 2783–2787.

[15] J. Frank and L. Schonherr, "WaveFake: A data set to facilitate au- ¨
dio deepfake detection," in Proc. Neural Information Processing Systems Datasets and Benchmarks Track, 2021.

[16] K. Ito, "The LJ speech dataset," https://keithito.com/LJ-SpeechDataset/, 2017.

[17] C. Veaux, J. Yamagishi, K. MacDonald *et al.*, "CSTR VCTK
corpus: English multi-speaker corpus for CSTR voice cloning toolkit," *University of Edinburgh. The Centre for Speech Technology Research (CSTR)*, 2017.

[18] H. Zen, V. Dang, R. Clark, Y. Zhang, R. J. Weiss, Y. Jia, Z. Chen, and Y. Wu, "LibriTTS: A corpus derived from librispeech for textto-speech," *Proc. Interspeech*, 2019.

[19] E. Bakhturina, V. Lavrukhin, B. Ginsburg, and Y. Zhang, "Hi-Fi multi-speaker english TTS dataset," in *Proc. Interspeech*, 2021, pp. 2776–2780.

[20] V. Panayotov, G. Chen, D. Povey, and S. Khudanpur, "LibriSpeech: an ASR corpus based on public domain audio books,"
in 2015 IEEE International Conference on Acoustics, Speech and Signal Processing (ICASSP). IEEE, 2015, pp. 5206–5210.

[21] R. Ardila, M. Branson, K. Davis, M. Kohler, J. Meyer, M. Henretty, R. Morais, L. Saunders, F. Tyers, and G. Weber, "Common voice: A massively-multilingual speech corpus," in *Proc. Language Resources and Evaluation Conference*, 2020, pp. 4218–
4222.

[22] J. Kahn, M. Riviere, W. Zheng, E. Kharitonov, Q. Xu, P.-E. `
Mazare, J. Karadayi, V. Liptchinsky, R. Collobert, C. Fuegen ´
et al., "Libri-light: A benchmark for asr with limited or no supervision," in Proc. IEEE International Conference on Acoustics, Speech and Signal Processing (ICASSP), 2020, pp. 7669–7673.

[23] Z. Duan, H. Fang, B. Li, K. C. Sim, and Y. Wang, "The NUS sung and spoken lyrics corpus: A quantitative comparison of singing and speech," in *Proc. Asia-Pacific Signal and Information Processing Association Annual Summit and Conference*, 2013, pp.

1–9.

[24] R. Huang, F. Chen, Y. Ren, J. Liu, C. Cui, and Z. Zhao, "Multisinger: Fast multi-singer singing voice vocoder with a large-scale corpus," in *Proc. ACM International Conference on Multimedia*,
2021, pp. 3945–3954.

[25] S. Choi, W. Kim, S. Park, S. Yong, and J. Nam, "Children's song dataset for singing voice research," in *Proc. International Society* for Music Information Retrieval Conference (ISMIR), 2020.

[26] J. Wilkins, P. Seetharaman, A. Wahl, and B. Pardo, "VocalSet: A
singing voice dataset." in *Proc. International Society for Music* Information Retrieval Conference (ISMIR), 2018, pp. 468–474.

[27] J. Koguchi, S. Takamichi, and M. Morise, "PJS: Phonemebalanced japanese singing-voice corpus," in Proc. Asia-Pacific Signal and Information Processing Association Annual Summit and Conference. IEEE, 2020, pp. 487–491.

[28] G. R. Dabike and J. Barker, "Automatic lyric transcription from karaoke vocal tracks: Resources and a baseline system." in *Proc.* Interspeech, 2019, pp. 579–583.

[29] S. Dai, S. Chen, Y. Wu, R. Diao, R. Huang, and R. B. Dannenberg, "Singstyle111: A multilingual singing dataset with style transfer," in *Proc. International Society for Music Information Retrieval Conference (ISMIR)*, 2023, pp. 4–2.

[30] B. Li, Y. Wang, and Z. Duan, "Audiovisual singing voice separation," *Transactions of the International Society for Music Information Retrieval (TISMIR)*, Nov 2021.

[31] J. F. Montesinos, V. S. Kadandale, and G. Haro, "A cappella:
Audio-visual singing voice separation," in Proc. British Machine Vision Conference (BMVC), 2021.

[32] Y. Xie, J. Zhou, X. Lu, Z. Jiang, Y. Yang, H. Cheng, and L. Ye,
"FSD: An initial chinese dataset for fake song detection," in Proc.

IEEE International Conference on Acoustics, Speech and Signal Processing (ICASSP), 2024.

[33] J.-w. Jung, H.-S. Heo, H. Tak, H.-j. Shim, J. S. Chung, B.-J. Lee, H.-J. Yu, and N. Evans, "AASIST: Audio anti-spoofing using integrated spectro-temporal graph attention networks," in *Proc. IEEE*
International Conference on Acoustics, Speech and Signal Processing (ICASSP), 2022, pp. 6367–6371.

[34] A. Pavao, I. Guyon, A.-C. Letournel, D.-T. Tran, X. Baro, H. J. Escalante, S. Escalera, T. Thomas, and Z. Xu, "Codalab competitions: An open source platform to organize scientific challenges," *Journal of Machine Learning Research*,
vol. 24, no. 198, pp. 1–6, 2023. [Online]. Available: http:
//jmlr.org/papers/v24/21-1436.html