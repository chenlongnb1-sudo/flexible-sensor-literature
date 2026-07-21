# Flexible Dual-Modal Sensing Transistor Enabled by Deep Learning Decoupling for Independent Light and Temperature Reconstruction

- 期刊：Nano-Micro Letters
- 日期：2026-07-07
- DOI：10.1007/s40820-026-02285-7
- 解析状态：fulltext_draft

## 摘要与研究价值

**Original:** Abstract Herein, a flexible dual-modal sensing transistor (FDST) is reported, based on zinc oxide nanofibers (ZnO NFs) integrated onto an indium–gallium–zinc–oxide thin-film transistor, and combined with a deep learning-based signal decoupling strategy. Defect-mediated subgap excitation and thermally activated interfacial potential modulation enable high sensitivity dual-modal responses, delivering a broadband photoresponsivity ( $$R$$ R ) up to 2.69 A W −1 and a temperature coefficient ( $${TC}$$ TC ) of 0.071 °C −1 . To enable reliable discrimination and simultaneous reconstruction of light and temperature, a multibias readout physically encodes the coupled stimuli into a high-dimensional current fingerprint, which is decoded by a lightweight multilayer perceptron. This synergistic approach enables accurate and independent reconstruction of light intensity and temperature, achieving coefficients of determination ( R 2 ) around 0.99. The FDST exhibits exceptional mechanical robustness under 10,000 bending cycles and severe bending (2 mm radius). Furthermore, a wearable system based on a low-power microcontroller demonstrates real-time monitoring with negligible cross-interference between optical and thermal modalities under uncontrolled outdoor conditions. This work establishes a general strategy for resolving cross-sensitivity, paving the way for robust and intelligent artificial perception systems.

**中文:** 涉及坏点、漂移、跨器件迁移或少样本校准；提供机器人、可穿戴或电子皮肤系统任务证据。摘要可核实数值包括：2.69 A、2 mm。

## 创新点

- Abstract Herein, a flexible dual-modal sensing transistor (FDST) is reported, based on zinc oxide nanofibers (ZnO NFs) integrated onto an indium–gallium–zinc–oxide thin-film transistor, and combined with a deep learning-based signal decoupling strategy.
- 涉及坏点、漂移、跨器件迁移或少样本校准
- 提供机器人、可穿戴或电子皮肤系统任务证据

## 对当前课题的启发

- 涉及坏点、漂移、跨器件迁移或少样本校准
- 提供机器人、可穿戴或电子皮肤系统任务证据
- 可对照 raw pixel、software feature 与 physical projection 的性能/通道/功耗
- 在同一阵列上比较 raw scanning、software feature 与低通道 hardware macro-pixel，量化通道数、延迟、功耗和任务精度。
- 把其传感源端的物理编码或抗干扰机制抽象为 ADC 前投影，对比源端输出与采样后软件补偿的信噪比和通道成本。

## 制备与实验步骤

### 1. 制备与实验操作

**Source:** p.4

**Original:** Among all conditions, the fibers fabricated at 15 kV exhibit the smallest standard deviation (37.6 nm), compared to 49.0 nm at 17 kV.

**中文:** 制备与实验操作步骤，关键配比、时间、温度和设备参数以 p.4 原文为准。

### 2. 材料混合与分散

**Source:** p.4

**Original:** When the voltage is further increased to 17 kV, a slight increase in diameter dispersion is observed, which is likely associated with jet instability and enhanced whipping behavior under an excessively strong electric field.

**中文:** 材料混合与分散步骤，关键配比、时间、温度和设备参数以 p.4 原文为准。

### 3. 固化与热处理

**Source:** p.4

**Original:** The effect of annealing treatment on fiber morphology was analyzed using atomic force microscopy (AFM), as shown in Fig. S4.

**中文:** 固化与热处理步骤，关键配比、时间、温度和设备参数以 p.4 原文为准。

### 4. 固化与热处理

**Source:** p.4

**Original:** The AFM height profiles indicate a clear morphological evolution after annealing, while the measured root-mean-square (RMS) roughness remains nearly unchanged.

**中文:** 固化与热处理步骤，关键配比、时间、温度和设备参数以 p.4 原文为准。

### 5. 成膜与沉积

**Source:** p.4

**Original:** An optimal electrospinning deposition time of 40 s is identified for the ZnO NFs (Fig. S5 and Note S1).

**中文:** 成膜与沉积步骤，关键配比、时间、温度和设备参数以 p.4 原文为准。

### 6. 图形化与结构成形

**Source:** p.4

**Original:** c XRD pattern of the ZnO NFs.

**中文:** 图形化与结构成形步骤，关键配比、时间、温度和设备参数以 p.4 原文为准。

### 7. 图形化与结构成形

**Source:** p.4

**Original:** g Relative content of VO and M–OH as a function of etching time.

**中文:** 图形化与结构成形步骤，关键配比、时间、温度和设备参数以 p.4 原文为准。

### 8. 图形化与结构成形

**Source:** p.4

**Original:** i UPS spectra of the ZnO and IGZO layers evolution of In, Ga, Zn, and O as a function of etching time is presented in Fig. S6.

**中文:** 图形化与结构成形步骤，关键配比、时间、温度和设备参数以 p.4 原文为准。

### 9. 图形化与结构成形

**Source:** p.4

**Original:** The evolution of O 1s spectra during the etching process is shown in Fig. 2e.

**中文:** 图形化与结构成形步骤，关键配比、时间、温度和设备参数以 p.4 原文为准。

### 10. 组装与封装

**Source:** p.4

**Original:** By combining the UPS-derived parameters with the optical bandgaps obtained from Tauc analysis, the complete energy level alignment of the ZnO/IGZO heterojunction was constructed (Fig. S8).

**中文:** 组装与封装步骤，关键配比、时间、温度和设备参数以 p.4 原文为准。

### 11. 制备与实验操作

**Source:** p.6

**Original:** 3.2 Optical Sensing Performance of the FDST To clarify the role of the ZnO NFs sensing layer, a pristine IGZO TFT and a fabricated FDST are first presented in Fig. S9.

**中文:** 制备与实验操作步骤，关键配比、时间、温度和设备参数以 p.6 原文为准。

### 12. 组装与封装

**Source:** p.6

**Original:** The transfer curves of nine devices are shown in Fig. S10a, from which the average saturation mobility is 11.65 ± 0.24 cm2 V−1 s−1, the threshold voltage (Vth) is 1.15 ± 0.18 V, the Ion/Ioff ratio is (1.35 ± 0.85) × 108, and the subthreshold swing is 0.44 ± 0.01 V dec−1.

**中文:** 组装与封装步骤，关键配比、时间、温度和设备参数以 p.6 原文为准。

### 13. 组装与封装

**Source:** p.6

**Original:** The transfer curves remain largely overlapped during cycling, while the dual-sweep curves show negligible displacement.

**中文:** 组装与封装步骤，关键配比、时间、温度和设备参数以 p.6 原文为准。

### 14. 组装与封装

**Source:** p.6

**Original:** As shown in Fig. S11a, the transfer characteristics of the pristine IGZO TFT measured under dark conditions and under whitelight illumination with intensities ranging from 0.1 to 1 mW mm−2 are nearly identical, indicating negligible photoresponse in the absence of the ZnO sensing layer.

**中文:** 组装与封装步骤，关键配比、时间、温度和设备参数以 p.6 原文为准。

### 15. 组装与封装

**Source:** p.6

**Original:** As the light intensity increases from dark to 1 mW mm−2, the transfer curves shift progressively toward negative gate voltage.

**中文:** 组装与封装步骤，关键配比、时间、温度和设备参数以 p.6 原文为准。

### 16. 组装与封装

**Source:** p.6

**Original:** a Transfer characteristics measured under different white-light illumination intensities.

**中文:** 组装与封装步骤，关键配比、时间、温度和设备参数以 p.6 原文为准。

## 方法原文锚点

<a id="M001"></a>
**Source:** p.4 M001

**Original:** For the ZnO NFs sensing layer, electrospun nanofibers were employed to provide a high surface-to-volume ratio and enhanced environmental interaction, making their microstructural uniformity critical for stable sensing performance [40–43]. Fiber diameter distributions obtained under different electrospinning voltages are shown in Fig. S2, and the corresponding statistical results are summarized in Fig. S3 as mean ± standard deviation (SD). With increasing electrospinning voltage from 8 to 17 kV, the average fiber diameter decreases monotonically from 644.6 ± 111.3 to 547.7 ± 49.0 nm. Among all conditions, the fibers fabricated at 15 kV exhibit the smallest standard deviation (37.6 nm), compared to 49.0 nm at 17 kV. Although the average diameters at 15 and 17 kV are comparable, the diameter distribution at 15 kV is narrower and more symmetric, indicating improved structural uniformity of the ZnO NFs. When the voltage is further increased to 17 kV, a slight increase in diameter dispersion is observed, which is likely associated with jet instability and enhanced whipping behavior under an excessively strong electric field. Based on these results, and considering the improved structural uniformity, 15 kV was selected as the optimal electrospinning voltage for subsequent experiments. The effect of annealing treatment on fiber morphology was analyzed using atomic force microscopy (AFM), as shown in Fig. S4. The AFM height profiles indicate a clear morphological evolution after annealing, while the measured root-mean-square (RMS) roughness remains nearly unchanged. This morphological evolution is mainly attributed to the removal of residual solvents and organic components from the precursor, resulting in a stable inorganic fiber framework. Large-area optical microscopy (Fig. 2b) confirms that the electrospun ZnO NFs form a random yet continuous network under the optimized processing conditions. The ZnO NFs were characterized by X-ray diffraction (XRD), as shown in Fig. 2c. All diffraction peaks can be indexed to the hexagonal wurtzite phase of ZnO (JCPDS No. 36-1451), with no detectable impurity-related phases. An optimal electrospinning deposition time of 40 s is identified for the ZnO NFs (Fig. S5 and Note S1). To resolve the spatial distribution of elements within the heterostructure, X-ray photoelectron spectroscopy (XPS) depth profiling was performed. The atomic concentration

**中文:** 该段已进入结构化方法步骤；完整逐段翻译待智能体精读补齐。

<a id="M002"></a>
**Source:** p.5 M002

**Original:** Nano-Micro Lett. (2026) 18:429 Page 5 of 18 429

**中文:** 该段已进入结构化方法步骤；完整逐段翻译待智能体精读补齐。

<a id="M003"></a>
**Source:** p.5 M003

**Original:** Fig. 2 Structural architecture and material characterization of the FDST. a Schematic illustration of the FDST structure and layer stack. b Optical microscope image of the electrospun ZnO NFs network. c XRD pattern of the ZnO NFs. d Deconvoluted O 1s XPS spectrum of the ZnO sensing layer. e Depth-dependent O 1s XPS spectra across the ZnO/IGZO stack presented as a waterfall plot. f Deconvoluted O 1s XPS spectrum of the IGZO layer. g Relative content of VO and M–OH as a function of etching time. h UV–Vis absorption spectra of ZnO and IGZO measured over the wavelength range of 250–900 nm after linear background subtraction and normalization. i UPS spectra of the ZnO and IGZO layers

**中文:** 该段已进入结构化方法步骤；完整逐段翻译待智能体精读补齐。

<a id="M004"></a>
**Source:** p.5 M004

**Original:** evolution of In, Ga, Zn, and O as a function of etching time is presented in Fig. S6. A sharp decrease in the Zn signal at approximately 800 s, accompanied by the emergence and stabilization of In and Ga signals, clearly identifies the transition from the ZnO nanofiber layer to the underlying IGZO channel. Based on the compositional transition identified from depth profiling, high-resolution O 1s spectra were extracted for the ZnO and IGZO regions. The O 1s spectrum of the ZnO layer (Fig. 2d) can be deconvoluted into

**中文:** 该段已进入结构化方法步骤；完整逐段翻译待智能体精读补齐。

<a id="M005"></a>
**Source:** p.5 M005

**Original:** three components centered at 530.0 ± 0.2, 531.0 ± 0.2, and 532.0 ± 0.2 eV, corresponding to lattice oxygen (M–O), oxygen vacancy (VO), and surface hydroxyl species (M–OH), with relative fractions of 46.13%, 31.07%, and 22.80%, respectively. In contrast, the O 1s spectrum of the IGZO layer (Fig. 2f) is dominated by lattice oxygen (83.74%), while VO and M–OH components account for only 13.48% and 2.78%, respectively. This marked difference between the two regions reflects distinct chemical-state distributions

**中文:** 该段已进入结构化方法步骤；完整逐段翻译待智能体精读补齐。

<a id="M006"></a>
**Source:** p.6 M006

**Original:** Nano-Micro Lett. (2026) 18:429 429 Page 6 of 18

**中文:** 该段已进入结构化方法步骤；完整逐段翻译待智能体精读补齐。

<a id="M007"></a>
**Source:** p.6 M007

**Original:** https://doi.org/10.1007/s40820-026-02285-7 © The authors

**中文:** 该段已进入结构化方法步骤；完整逐段翻译待智能体精读补齐。

<a id="M008"></a>
**Source:** p.6 M008

**Original:** across the heterostructure. The evolution of O 1s spectra during the etching process is shown in Fig. 2e. The spectral shape remains stable within the ZnO region and progressively shifts as the interface is approached, before stabilizing again in the IGZO region. The quantitative depth-dependent variation of oxygen-related components is summarized in Fig. 2g, where the fractions of VO and M–OH decrease sharply after crossing the interface. The consistent trends observed in both spectral evolution and quantitative analysis further confirm the well-defined stratification of the ZnO/ IGZO stack. The optical absorption spectra of ZnO and IGZO are shown in Fig. 2h. For reliable spectral comparison, the spectra were processed by linear background subtraction followed by normalization prior to analysis. The corresponding Tauc plots derived from these spectra are presented in Fig. S7, from which the optical bandgaps were extracted as 2.71 and 3.57 eV, respectively. Ultraviolet photoelectron spectroscopy (UPS) was employed to determine the electronic energy levels (Fig. 2i). The secondary electron cutoff energies (Ecut-off) are 17.07 eV for ZnO and 17.42 eV for IGZO. Using Φ = hν − Ecut-off (hν = 21.22 eV), the corresponding work functions are calculated to be approximately 4.15 and 3.80 eV, respectively. The valence band maxima (EVBM) relative to the Fermi level are 2.61 eV for ZnO and 3.04 eV for IGZO. By combining the UPS-derived parameters with the optical bandgaps obtained from Tauc analysis, the complete energy level alignment of the ZnO/IGZO heterojunction was constructed (Fig. S8).

**中文:** 该段已进入结构化方法步骤；完整逐段翻译待智能体精读补齐。

<a id="M009"></a>
**Source:** p.6 M009

**Original:** 3.2 Optical Sensing Performance of the FDST

**中文:** 该段已进入结构化方法步骤；完整逐段翻译待智能体精读补齐。

<a id="M010"></a>
**Source:** p.6 M010

**Original:** To clarify the role of the ZnO NFs sensing layer, a pristine IGZO TFT and a fabricated FDST are first presented in Fig. S9. Both devices share an identical layer structure and channel geometry, except for the presence of the ZnO NFs in the FDST. The channel length (L) and width (W) are 150 and 1000 μm, respectively. The electrical properties of the FDST were evaluated under dark conditions. The transfer curves of nine devices are shown in Fig. S10a, from which the average saturation mobility is 11.65 ± 0.24 cm2 V−1 s−1, the threshold voltage (Vth) is 1.15 ± 0.18 V, the Ion/Ioff ratio is (1.35 ± 0.85) × 108, and the subthreshold swing is 0.44 ± 0.01 V dec−1. Continuous cyclic testing for 3000 cycles (Fig. S10b) and dual-sweep measurement (Fig. S10c) were also performed

**中文:** 该段已进入结构化方法步骤；完整逐段翻译待智能体精读补齐。

<a id="M011"></a>
**Source:** p.6 M011

**Original:** to evaluate operational stability and hysteresis. The transfer curves remain largely overlapped during cycling, while the dual-sweep curves show negligible displacement. Control experiments were further conducted using a pristine IGZO TFT to identify the source of the multimodal response. As shown in Fig. S11a, the transfer characteristics of the pristine IGZO TFT measured under dark conditions and under whitelight illumination with intensities ranging from 0.1 to 1 mW mm−2 are nearly identical, indicating negligible photoresponse in the absence of the ZnO sensing layer. In contrast, the FDST incorporating electrospun ZnO NFs exhibits pronounced light-dependent modulation (Fig. 3a). As the light intensity increases from dark to 1 mW mm−2, the transfer curves shift progressively toward negative gate voltage. This systematic shift confirms that optical excitation modulates channel conductivity through the ZnO sensing layer. To comprehensively quantify the photodetection performance, three key metrics were introduced: photoresponsivity ( R ), photosensitivity ( S ), and apparent specific detectivity ( D∗ app ) [44–46].

**中文:** 该段已进入结构化方法步骤；完整逐段翻译待智能体精读补齐。

<a id="M012"></a>
**Source:** p.6 M012

**Original:** Under broadband white-light illumination, R and S are defined as:

**中文:** 该段已进入结构化方法步骤；完整逐段翻译待智能体精读补齐。

<a id="M013"></a>
**Source:** p.6 M013

**Original:** Ilight −Idark

**中文:** 该段已进入结构化方法步骤；完整逐段翻译待智能体精读补齐。

<a id="M014"></a>
**Source:** p.6 M014

**Original:** (1) R =

**中文:** 该段已进入结构化方法步骤；完整逐段翻译待智能体精读补齐。

<a id="M015"></a>
**Source:** p.6 M015

**Original:** Pin ⋅A

**中文:** 该段已进入结构化方法步骤；完整逐段翻译待智能体精读补齐。

<a id="M016"></a>
**Source:** p.6 M016

**Original:** Ilight Idark

**中文:** 该段已进入结构化方法步骤；完整逐段翻译待智能体精读补齐。

<a id="M017"></a>
**Source:** p.6 M017

**Original:** (2) S =

**中文:** 该段已进入结构化方法步骤；完整逐段翻译待智能体精读补齐。

<a id="M018"></a>
**Source:** p.6 M018

**Original:** Here, Ilight and Idark denote the drain current under illumination and in the dark, respectively; Pin is the incident white-light power density; A is the effective illuminated area, which was defined by a physical aperture mask exposing only the FDST channel region. Based on these definitions, the FDST exhibits a maximum broadband R of 2.69 A W−1 in the saturation regime, reflecting efficient photocarrier generation and collection. Under weak illumination at gate voltage (VG) = 0 V, the S reaches 6.96 × 103, ensuring a high signal-to-noise ratio in optical signal readout. To evaluate the noise-limited detection capability, the dark-current fluctuation was experimentally characterized at a representative operating condition (VG = − 0.1 V). As shown in Fig. S12, the time-domain dark-current traces exhibit stable fluctuations without noticeable drift, and the corresponding histograms follow Gaussian-like distributions, indicating stationary noise behavior. The root-mean-square (RMS) noise

**中文:** 该段已进入结构化方法步骤；完整逐段翻译待智能体精读补齐。

<a id="M019"></a>
**Source:** p.7 M019

**Original:** Nano-Micro Lett. (2026) 18:429 Page 7 of 18 429

**中文:** 该段已进入结构化方法步骤；完整逐段翻译待智能体精读补齐。

<a id="M020"></a>
**Source:** p.7 M020

**Original:** Fig. 3 Optical sensing performance and mechanism of the FDST. a Transfer characteristics measured under different white-light illumination intensities. b Dynamic drain-current response under sequential light-intensity modulation. c Transient drain-current response to a single light on/ off pulse. d Repetitive drain-current response under periodic white-light illumination, with insets showing enlarged cycles. e Schematic of subgap defect excitation and carrier trapping in ZnO under white-light illumination. f FEA-simulated potential distribution in the ZnO/IGZO stack as a function of light intensity. g Benchmark comparison of responsivity versus response time with representative reports

**中文:** 该段已进入结构化方法步骤；完整逐段翻译待智能体精读补齐。

<a id="M021"></a>
**Source:** p.7 M021

**Original:** ( Ii −I )2 where B is the effective noise bandwidth. Based on the experimentally extracted parameters summarized in Table S1, the FDST exhibits an apparent specific detectivity of 1.1 × 108 Jones. Following recent guidelines for photodetector evaluation, this value is reported as D∗ app , as it is derived from time-domain noise analysis rather than a

**中文:** 该段已进入结构化方法步骤；完整逐段翻译待智能体精读补齐。

<a id="M022"></a>
**Source:** p.7 M022

**Original:** current was extracted from the steady-state current fluctuation, defined as:

**中文:** 该段已进入结构化方法步骤；完整逐段翻译待智能体精读补齐。

<a id="M023"></a>
**Source:** p.7 M023

**Original:** √ √ √ √ 1 N −1

**中文:** 该段已进入结构化方法步骤；完整逐段翻译待智能体精读补齐。

<a id="M024"></a>
**Source:** p.7 M024

**Original:** N ∑

**中文:** 该段已进入结构化方法步骤；完整逐段翻译待智能体精读补齐。

<a id="M025"></a>
**Source:** p.7 M025

**Original:** (3) irms =

**中文:** 该段已进入结构化方法步骤；完整逐段翻译待智能体精读补齐。

<a id="M026"></a>
**Source:** p.7 M026

**Original:** i=1

**中文:** 该段已进入结构化方法步骤；完整逐段翻译待智能体精读补齐。

<a id="M027"></a>
**Source:** p.7 M027

**Original:** where I is the average current over the selected steady-state time window. The D∗ app can thus be written as:

**中文:** 该段已进入结构化方法步骤；完整逐段翻译待智能体精读补齐。

<a id="M028"></a>
**Source:** p.7 M028

**Original:** √

**中文:** 该段已进入结构化方法步骤；完整逐段翻译待智能体精读补齐。

<a id="M029"></a>
**Source:** p.7 M029

**Original:** (4) D∗ app = R

**中文:** 该段已进入结构化方法步骤；完整逐段翻译待智能体精读补齐。

<a id="M030"></a>
**Source:** p.7 M030

**Original:** AB irms

**中文:** 该段已进入结构化方法步骤；完整逐段翻译待智能体精读补齐。

<a id="M031"></a>
**Source:** p.8 M031

**Original:** Nano-Micro Lett. (2026) 18:429 429 Page 8 of 18

**中文:** 该段已进入结构化方法步骤；完整逐段翻译待智能体精读补齐。

<a id="M032"></a>
**Source:** p.8 M032

**Original:** https://doi.org/10.1007/s40820-026-02285-7 © The authors

**中文:** 该段已进入结构化方法步骤；完整逐段翻译待智能体精读补齐。

<a id="M033"></a>
**Source:** p.8 M033

**Original:** rigorous frequency-domain noise characterization or an evaluation based on noise equivalent power [46]. The lightintensity-resolving capability was examined under stepwise and mixed-intensity sequences (Fig. 3b). Distinct steadystate current plateaus are observed and correlate with the incident white-light intensity. Notably, when high-intensity pulses are inserted into a sequence with random intensity fluctuations, the current rapidly returns to the steady-state level corresponding to the subsequent lower intensity without discernible hysteresis or residual memory. The transient response under a single light-intensity step is shown in Fig. 3c. The rise time (τrise) and relax time (τrelax) are defined as the durations required for the current to transition between 10 and 90% of the response amplitude [44, 45]. These two key threshold levels are defined as follows:

**中文:** 该段已进入结构化方法步骤；完整逐段翻译待智能体精读补齐。

<a id="M034"></a>
**Source:** p.8 M034

**Original:** (5) I90% = Imin + (Imax −Imin ) × 0.9

**中文:** 该段已进入结构化方法步骤；完整逐段翻译待智能体精读补齐。

<a id="M035"></a>
**Source:** p.8 M035

**Original:** (6) I10% = Imin + (Imax −Imin ) × 0.1

**中文:** 该段已进入结构化方法步骤；完整逐段翻译待智能体精读补齐。

<a id="M036"></a>
**Source:** p.8 M036

**Original:** Here, Imax and Imin represent the steady-state current after stimulus application (maximum response) and the initial baseline current, respectively. Based on this definition, the FDST exhibits rapid current transitions when illumination is switched on or off: τrise and τrelax are as short as 83 and 110 ms, respectively. Long-term cycling stability was evaluated under a white-light intensity of 1 mW cm−2 at a switching frequency of 0.1 Hz (Fig. 3d). Quantitative analysis based on the extracted current values reveals that the average on-state current decreases by only 2.8% after 100 cycles, indicating highly stable and reproducible optical switching behavior. The enlarged views of representative early and late cycles further confirm the nearly identical waveform characteristics, demonstrating the robust operational stability of the device. The opticalresponse mechanism is illustrated in Fig. 3e. Oxygenvacancy-related subgap defect states in ZnO introduce localized levels within the bandgap, enabling visible-light absorption below the intrinsic bandgap energy [47–49]. To further support this defect-mediated interpretation, the spectral distribution of the white LED used in Fig. 3a is provided in Fig. S13, confirming broadband emission in the visible range. In addition, wavelength-dependent transient photocurrent responses under monochromatic illumination at 405, 532 and 635 nm are presented in Fig. S14. Clear and reversible responses are observed at all three wavelengths, consistent with defect-assisted subgap excitation in the ZnO NFs sensing layer. Under illumination,

**中文:** 该段已进入结构化方法步骤；完整逐段翻译待智能体精读补齐。

<a id="M037"></a>
**Source:** p.8 M037

**Original:** photogenerated holes are preferentially trapped by deep defect states and act as fixed positive charge centers, elevating the local electrostatic potential of the ZnO layer [50, 51]. Through capacitive coupling across the ZnO/ IGZO interface, this light-induced surface potential effectively acts as an additional internal gate bias. Specifically, the accumulation of trapped positive charges lowers the potential barrier for electron transport in the underlying IGZO channel, leading to the observed negative Vth shift rather than a direct increase in bulk channel conductance. This photogating-dominated response is consistent with the parallel shift of the transfer curves and the nearly constant on-state drain current observed in Fig. 3a [52]. Finite element analysis (FEA) was conducted to simulate the light-intensity-dependent potential distribution within the ZnO/IGZO stack (Fig. 3f). In the model, light-induced surface-charge modulation was applied exclusively to the ZnO layer, and the resulting electrostatic potential was self-consistently propagated to the underlying IGZO channel through capacitive coupling. The simulation solves the Poisson equation with surface-charge boundary conditions, and the detailed governing equations and phenomenological descriptions are provided in Table S2 and Note S2. Using a saturation-type light-dependent surface-charge model, the simulated potential maps show a monotonic increase in surface and interfacial potential with increasing illumination intensity, consistent with the experimentally observed light-induced conductivity enhancement. To benchmark the overall white-light photodetection performance, responsivity versus response time is compared with representative white-light photodetectors reported in the literature (Fig. 3g and Table S3) [53–63]. The FDST resides in a region characterized by a balanced combination of high responsivity and relatively fast response dynamics.

**中文:** 该段已进入结构化方法步骤；完整逐段翻译待智能体精读补齐。

<a id="M038"></a>
**Source:** p.8 M038

**Original:** 3.3 Thermal Sensing Performance of the FDST

**中文:** 该段已进入结构化方法步骤；完整逐段翻译待智能体精读补齐。

<a id="M039"></a>
**Source:** p.8 M039

**Original:** The temperature-dependent electrical characteristics of the FDST were systematically examined over the range of 20–80 °C. For comparison, a pristine IGZO TFT without ZnO nanofiber integration was measured under identical conditions. As shown in Fig. S11b, the transfer curves of the reference device remain nearly unchanged across the

**中文:** 该段已进入结构化方法步骤；完整逐段翻译待智能体精读补齐。

<a id="M040"></a>
**Source:** p.9 M040

**Original:** Nano-Micro Lett. (2026) 18:429 Page 9 of 18 429

**中文:** 该段已进入结构化方法步骤；完整逐段翻译待智能体精读补齐。

<a id="M041"></a>
**Source:** p.9 M041

**Original:** entire temperature range, indicating that the IGZO channel itself exhibits negligible intrinsic thermal sensitivity. In contrast, the FDST displays a clear and continuous modulation of its transfer characteristics with increasing temperature. As shown in Fig. 4a, the transfer curves shift progressively toward negative gate voltage, accompanied by a monotonic increase in the turn-on current. This systematic evolution reflects an enhancement of channel conductivity induced by thermal stimulation. We employ the temperature coefficient ( TC ) to quantify the device’s thermal response, defined as:

**中文:** 该段已进入结构化方法步骤；完整逐段翻译待智能体精读补齐。

<a id="M042"></a>
**Source:** p.9 M042

**Original:** (7) TC = ΔI∕I0

**中文:** 该段已进入结构化方法步骤；完整逐段翻译待智能体精读补齐。

<a id="M043"></a>
**Source:** p.9 M043

**Original:** ΔT × 100%

**中文:** 该段已进入结构化方法步骤；完整逐段翻译待智能体精读补齐。

<a id="M044"></a>
**Source:** p.9 M044

**Original:** where I0 is the drain current at the initial temperature, ΔI represents the temperature-induced current variation, and ΔT is the corresponding temperature change [64]. Within the tested range, the FDST exhibits a TC of 0.071 °C−1 in its typical operating state. Dynamic tests under sequential temperature modulations (Fig. 4b) demonstrate the device’s ability to distinguish varying thermal gradients, where the current plateaus accurately correspond to specific temperature increments (ΔT from 0.5 to 5.0 °C). The stepwise temperature response (Fig. 4c) further confirms the thermal tracking capability of the FDST. Using the same criteria defined in Eqs. (5) and (6), the FDST maintains a secondlevel response speed (τrise ≈ 0.36 s; τrelax ≈ 1.52 s), despite the inherently slower ionic relaxation involved in thermochemical processes, enabling it to effectively capture rapid fluctuations in ambient temperature fields. Long-term stability under repeated thermal switching is shown in Fig. 4d, where the averaged steady-state drain current for each cycle is plotted over 100 cycles between 30 and 40 °C. The FDST exhibits negligible degradation, with the relative variation remaining within 1.5% and no observable monotonic decay trend. Enlarged views further confirm nearly unchanged amplitude and waveform shape, demonstrating excellent cyclic stability. The thermally induced interfacial modulation mechanism is illustrated in Fig. 4e. In the initial state, the ZnO surface is rich in adsorbed oxygen species ( O− 2 ) and hydroxyl groups (–OH), which introduce electron trapping on the surface of the n-type semiconductor. The resulting negatively charged surface layer establishes an electrostatic potential that induces upward band bending and electron depletion in the IGZO channel through capacitive coupling, thereby suppressing the dark-state conductivity [65]. Upon thermal stimulation, surface adsorption–desorption processes are activated on the ZnO surface. In particular, the desorption of surface-adsorbed oxygen species releases

**中文:** 该段已进入结构化方法步骤；完整逐段翻译待智能体精读补齐。

<a id="M045"></a>
**Source:** p.9 M045

**Original:** previously trapped electrons back into the conduction band [66–68], as described below:

**中文:** 该段已进入结构化方法步骤；完整逐段翻译待智能体精读补齐。

<a id="M046"></a>
**Source:** p.9 M046

**Original:** (8) O− 2 (ads) ⇌O2(g) + e−

**中文:** 该段已进入结构化方法步骤；完整逐段翻译待智能体精读补齐。

<a id="M047"></a>
**Source:** p.9 M047

**Original:** where ads and g denote the adsorbed and gaseous states, respectively. As the O− 2 species desorb, the electron depletion layer at the surface becomes thinner, leading to increased carrier concentration. Meanwhile, surface –OH undergoes a dehydration condensation reaction. Driven primarily by thermal activation, this dehydroxylation process is enabled by the thermal energy supplied at elevated temperatures, which facilitates the removal of surface hydroxyl groups and the healing of surface VO [69]. The reaction kinetics are described as follows:

**中文:** 该段已进入结构化方法步骤；完整逐段翻译待智能体精读补齐。

<a id="M048"></a>
**Source:** p.9 M048

**Original:** (9) 2OH−(ads) ⇌H2O(g) + O2−(lattice)

**中文:** 该段已进入结构化方法步骤；完整逐段翻译待智能体精读补齐。

<a id="M049"></a>
**Source:** p.9 M049

**Original:** The O2− generated in the forward reaction refills VO at the surface, is electrostatically compensated by the lattice field, and no longer acts as an additional negative charge center. The reduction in surface negative charge density leads to a gradual flattening of the upward band bending and a positive shift in the interfacial electrostatic potential, which is capacitively coupled to the IGZO channel as a temperature-dependent electrical modulation. When the heat source is removed (cooling) or the device returns to its initial equilibrium state, the above reactions proceed in reverse, leading to the reformation of the surface depletion layer and endowing the device with good reversibility. Figure 4f, with detailed data listed in Table S4, presents a six-dimensional comparison between the FDST and representative flexible temperature sensors [70–73], encompassing sensitivity, response and recovery times, resolution, temperature range, and bending cycles. Rather than excelling in a single parameter, the FDST maintains competitive performance across all metrics, highlighting its multiparameter optimization. As the thermal response is closely related to surface adsorption–desorption processes, the influence of ambient humidity (relative humidity, RH) was further evaluated. As shown in Fig. S15a–c, the transfer characteristics measured at 20, 40, and 60 °C under different RH levels (30%–70%) exhibit only minor variations, including a slight positive shift in threshold voltage and a marginal reduction in on-current as RH increases from 30% to 70%. The dynamic thermal responses under repeated temperature cycling (Fig. S15d) further demonstrate that the waveform shape and reversibility are well preserved across different RH conditions, with only a slight reduction in response amplitude

**中文:** 该段已进入结构化方法步骤；完整逐段翻译待智能体精读补齐。

<a id="M050"></a>
**Source:** p.10 M050

**Original:** Nano-Micro Lett. (2026) 18:429 429 Page 10 of 18

**中文:** 该段已进入结构化方法步骤；完整逐段翻译待智能体精读补齐。

<a id="M051"></a>
**Source:** p.10 M051

**Original:** Fig. 4 Thermal sensing performance and mechanism of the FDST. a Transfer characteristics measured under different temperatures. b Dynamic drain-current response under sequential temperature steps. c Transient drain-current response to a single-step thermal pulse. d Cycling stability under repeated temperature switching; insets show representative cycles. e Schematic illustration of thermally activated surface processes and capacitive coupling between ZnO and the IGZO channel. f Radar comparison of thermal sensing metrics among representative flexible temperature sensors. g FEA-simulated temperature-dependent potential distribution in the ZnO/IGZO stack

**中文:** 该段已进入结构化方法步骤；完整逐段翻译待智能体精读补齐。

<a id="M052"></a>
**Source:** p.10 M052

**Original:** https://doi.org/10.1007/s40820-026-02285-7 © The authors

**中文:** 该段已进入结构化方法步骤；完整逐段翻译待智能体精读补齐。

<a id="M053"></a>
**Source:** p.10 M053

**Original:** observed at higher humidity. The TC as a function of RH (Fig. S15e) shows a gradual decrease with increasing humidity. Notably, the TC at 80% RH exhibits a maximum reduction of approximately 13.7% compared to that at 30% RH. These results suggest that moisture introduces a bounded perturbation rather than significantly disrupting the thermally activated sensing mechanism. Finally, the temperature-dependent potential evolution was examined by FEA (Fig. 4g). Thermal modulation was introduced at the ZnO surface through

**中文:** 该段已进入结构化方法步骤；完整逐段翻译待智能体精读补齐。

<a id="M054"></a>
**Source:** p.10 M054

**Original:** a temperature-dependent surface-charge model, and the induced electrostatic variation was subsequently transferred to the IGZO channel via interfacial capacitive coupling. The governing equations and boundary conditions are summarized in Table S2 and Note S2, while the main text focuses on the agreement between simulation and experimental observations.

**中文:** 该段已进入结构化方法步骤；完整逐段翻译待智能体精读补齐。

<a id="M055"></a>
**Source:** p.11 M055

**Original:** Nano-Micro Lett. (2026) 18:429 Page 11 of 18 429

**中文:** 该段已进入结构化方法步骤；完整逐段翻译待智能体精读补齐。

<a id="M056"></a>
**Source:** p.11 M056

**Original:** 3.4 Mechanical Robustness and Response Stability under Dynamic Deformation

**中文:** 该段已进入结构化方法步骤；完整逐段翻译待智能体精读补齐。

<a id="M057"></a>
**Source:** p.11 M057

**Original:** To evaluate the mechanical tolerance and operational reliability of the FDST under dynamic deformation, systematic flexibility tests were performed using a customized bending platform (Fig. S16a). Figure S16b depicts the transfer characteristics measured before and after 10,000 bending cycles at a small bending radius of 2 mm under three combined photothermal conditions: darkness at 20 °C, 0.1 mW mm−2 at 40 °C, and 0.3 mW mm−2 at 60 °C. Notably, even after extensive mechanical fatigue, the on-current, subthreshold region, and off-state noise floor exhibited negligible degradation, demonstrating the stable operation of the FDST for long-term operation. Beyond basic electrical survival, we further evaluated whether mechanical strain perturbs the dual-modal sensing outputs. Under tensile bending (Fig. S17a), the maximum R (Max.R ) maintains a narrow range of 2.65–2.70 A W−1 across the entire bendingradius range (from 7 to 1 mm). The TC also remained stable (0.068–0.071 °C⁻1) without discernible drift. A consistent robustness was observed under compressive bending (Fig. S17b), where Max. R (2.64–2.71 A W−1) and TC (0.069–0.071 °C−1) exhibit only minor and reversible variations with curvature. To further examine the device morphology after repeated mechanical deformation, enlarged optical micrographs were recorded before and after 10,000 bending cycles (Fig. S18). No observable cracks or disruption of the ZnO nanofiber network were detected within the imaged region. These results collectively indicate that the FDST maintains stable photothermal transduction with limited sensitivity to mechanical deformation. Such robustness supports reliable dual-modal sensing under conditions relevant to flexible and wearable applications. To place the demonstrated performance in the context of existing multimodal sensing technologies, a quantitative comparison across key metrics is summarized in Table S5.

**中文:** 该段已进入结构化方法步骤；完整逐段翻译待智能体精读补齐。

<a id="M058"></a>
**Source:** p.11 M058

**Original:** 3.5 Multibias Electrical Fingerprinting for Stimulus Reconstruction

**中文:** 该段已进入结构化方法步骤；完整逐段翻译待智能体精读补齐。

<a id="M059"></a>
**Source:** p.11 M059

**Original:** Although the FDST exhibits pronounced conductance modulation under both optical and thermal stimuli, the drain current measured at a single gate bias does not provide a bijective mapping to the stimulus pair. As evidenced

**中文:** 该段已进入结构化方法步骤；完整逐段翻译待智能体精读补齐。

<a id="M060"></a>
**Source:** p.11 M060

**Original:** in Fig. S19, distinct light–temperature combinations may generate nearly identical current values at a specific bias despite corresponding to fundamentally different physical states. This degeneracy arises because the optical and thermal perturbations, though governed by distinct physical mechanisms, are projected onto a one-dimensional current axis where their responses partially overlap. To eliminate the intrinsic ambiguity associated with singlepoint sampling, we construct a three-bias readout vector X = [ID (− 3.3 V), ID (0 V), ID (+ 3.3 V)], which serves as a high-dimensional electrical fingerprint encoding the coupled optical–thermal response. These three gate biases were selected because they sample distinct regions of the transfer characteristics, exhibiting different sensitivities to optical and thermal perturbations. A detailed justification of this bias selection, together with a systematic ablation study over different bias combinations, is provided in Note S4 and Table S6, which confirms that the selected triplet achieves the optimal trade-off between decoupling accuracy and hardware constraints. This multibias strategy effectively transforms the modal coupling problem into a feature-separable representation problem, thereby rendering systematic model-based decoupling feasible. Recent IGZO-based sensing systems have increasingly incorporated machine learning and high-dimensional response engineering to enhance intelligent sensing and signal recognition. As summarized in Table S7, representative approaches include visual–tactile perception using IGZO TFTs integrated with an external triboelectric nanogenerator (TENG) [74], optoelectronic associative learning and neuromorphic pattern recognition in charge-trapping a-IGZO TFTs [75], optical-response-fingerprint-assisted gas recognition [76], and multidimensional gas discrimination based on complementary response signals from p-Cu2O/n-IGZO sensor arrays [77]. These approaches mainly rely on external modules, array-level architectures, or distinguishable response features for perception, classification, and neuromorphic learning. In contrast to these studies, our work focuses on coupled-stimulus decoupling and independent signal reconstruction within a single sensing channel. To determine the representational capacity required for accurate decoupling, we benchmarked several regression families with distinct modeling characteristics, including linear regression (LR), polynomial regression (PR), support vector regression (SVR), gradient-boosted decision trees (XGBoost), and an MLP (Fig. 5a) [77–79].

**中文:** 该段已进入结构化方法步骤；完整逐段翻译待智能体精读补齐。

<a id="M061"></a>
**Source:** p.12 M061

**Original:** Nano-Micro Lett. (2026) 18:429 429 Page 12 of 18

**中文:** 该段已进入结构化方法步骤；完整逐段翻译待智能体精读补齐。

<a id="M062"></a>
**Source:** p.12 M062

**Original:** https://doi.org/10.1007/s40820-026-02285-7 © The authors

**中文:** 该段已进入结构化方法步骤；完整逐段翻译待智能体精读补齐。

<a id="M063"></a>
**Source:** p.12 M063

**Original:** The corresponding architectures and mathematical formulations are detailed in Fig. S20 and Note S3. The coefficient of determination (R2) in Fig. 5b indicates that architectures beyond linear regression achieve higher predictive accuracy, suggesting that the mapping between electrical fingerprints and physical stimuli involves higher-order dependencies within this dataset. Among the candidates, the MLP yields the highest R2 for both light intensity and temperature, a result further supported by the minimal mean absolute error (MAE) shown in Fig. 5c. This consistent performance is corroborated by the final loss values summarized in Fig. S21 and the minimized mean squared error (MSE) shown in Fig. S22. Based on these evaluation results, a compact three-layer MLP (128–64–32 neurons) was implemented for final decoupling (Fig. 5d). The training loss rapidly converges within the first few hundred epochs (Fig. 5e), while the R2 during optimization consistently approaches unity (Fig. 5f). To visually compare the predictive behaviors across models, the parity plots for light intensity (0–5 mW/mm−2) are provided in Fig. S23 for LR, PR, SVR, and XGBoost, with the corresponding analysis for the MLP presented in Fig. 5g. Similarly, the parity plots for temperature (20–80 °C) for the alternative models are detailed in Fig. S24, while the MLP result is shown in Fig. 5h. On the independent test set, the MLP achieves R2 values of 0.992 and 0.989 for light intensity and temperature prediction, respectively. The narrow and symmetrically centered residual distributions (Fig. 5i) confirm unbiased and precise decoupling. To further evaluate modal decoupling, we first examined the residual trends with respect to the non-target modality, as shown in Fig. S25 [80]. In both cases, the residual distributions were smoothed using locally weighted scatterplot smoothing (LOWESS) to reveal the underlying trend, and the resulting curves remain nearly horizontal with only moderate fluctuations, indicating weak systematic dependence of the prediction errors on variations in the other sensing variable. To further quantify the decoupling performance, cross-sensitivity ( CS ), crosstalk error ( CE ), and modal orthogonality index ( OI ) were evaluated (definitions in Note S5). The values of CST←L and CSL←T were 0.11 °C (mW/mm2)−1 and 0.0028 mW mm−2 °C⁻1, respectively, while CET←L and CEL←T were 0.55 °C and 0.17 mW mm−2. In addition, the OI reached 0.94, indicating strong modal separation between the two sensing channels.

**中文:** 该段已进入结构化方法步骤；完整逐段翻译待智能体精读补齐。

<a id="M064"></a>
**Source:** p.12 M064

**Original:** 3.6 System Integration and Real‑World Environmental Monitoring

**中文:** 该段已进入结构化方法步骤；完整逐段翻译待智能体精读补齐。

<a id="M065"></a>
**Source:** p.12 M065

**Original:** Building upon the high-precision predictions of the MLPbased decoupling model, we developed a wearable sensing system capable of synchronous acquisition, decoupling, and real-time display of ambient light and temperature signals under practical usage conditions (Fig. 6a). To accommodate the wide dynamic range of drain currents spanning several orders of magnitude under different gate biases (VG = − 3.3, 0, and + 3.3 V), the system architecture incorporates a threechannel readout circuit with tailored gain settings. This configuration prevents amplifier saturation and ensures high-resolution signal acquisition across all operating regimes. The analog front-end utilizes transimpedance amplifiers (TIA, OPA657) for current-to-voltage conversion, followed by digitization via a multichannel 16-bit ADC (ADS1115). An STM32 microcontroller (MCU) collects the data and directly executes the pretrained MLP model to infer light intensity and temperature without the need for further retraining. Aligning with the intrinsic second-level response time of the FDST to thermal stimuli, the WDMS updates the displayed results at a 1 s interval, which effectively captures the real-time environmental variations while filtering out high-frequency noise. To rigorously validate the WDMS’s robustness under uncontrolled real-world conditions, we benchmarked our system against commercial sensors across three progressively challenging scenarios: baseline sunlight, shadow occlusion, and compound photothermal stimulation. The light intensity and temperature values were benchmarked against commercial reference instruments, namely a Thorlabs PM100D optical power meter (Thorlabs, USA) and a Fluke 54 II digital thermometer (Fluke Corporation, USA), respectively. Initially, under direct sunlight (Fig. 6b), the system demonstrated high-fidelity tracking, yielding values (21.8 °C, 12 mW cm−2) nearly identical to the commercial reference (22.0 °C, 12.5 mW cm−2), thereby establishing a solid accuracy baseline. Crucially, the system’s decoupling capability was tested by introducing a shadow (Fig. 6c). While the commercial sensor recorded a sharp illumination drop to 2.3 mW cm−2, our system accurately reproduced this transition (2 mW cm−2) without inducing any erroneous thermal drift (maintaining a stable output at 21.4 °C). This result highlights the independence of the predicted optical signal from thermal interference. Finally, in the

**中文:** 该段已进入结构化方法步骤；完整逐段翻译待智能体精读补齐。

<a id="M066"></a>
**Source:** p.13 M066

**Original:** Nano-Micro Lett. (2026) 18:429 Page 13 of 18 429

**中文:** 该段已进入结构化方法步骤；完整逐段翻译待智能体精读补齐。

<a id="M067"></a>
**Source:** p.13 M067

**Original:** Fig. 5 Evaluation and implementation of regression models for decoupled light intensity and temperature sensing. a Schematic comparison of regression algorithms, including LR, PR, SVR, XGBoost, and MLP. b R2 for light intensity and temperature prediction across models. c MAE for light intensity and temperature prediction across models. d Architecture of the MLP. e Training loss as a function of epoch for the MLP. f Evolution of R2 during MLP training. g Parity plot of predicted versus true light intensity using the MLP. h Parity plot of predicted versus true temperature using the MLP. i Residual distributions for MLP-based light intensity and temperature predictions

**中文:** 该段已进入结构化方法步骤；完整逐段翻译待智能体精读补齐。

<a id="M068"></a>
**Source:** p.13 M068

**Original:** most demanding scenario involving simultaneous intense irradiation and local heating (Fig. 6d), the system successfully resolved a high target temperature (38.8 °C) against a

**中文:** 该段已进入结构化方法步骤；完整逐段翻译待智能体精读补齐。

<a id="M069"></a>
**Source:** p.13 M069

**Original:** high-light background (13 mW cm−2), matching the reference (39.1 °C, 13.4 mW cm−2) with minimal error. This confirms that the MLP-based model achieves excellent modal

**中文:** 该段已进入结构化方法步骤；完整逐段翻译待智能体精读补齐。

<a id="M070"></a>
**Source:** p.14 M070

**Original:** Nano-Micro Lett. (2026) 18:429 429 Page 14 of 18

**中文:** 该段已进入结构化方法步骤；完整逐段翻译待智能体精读补齐。

<a id="M071"></a>
**Source:** p.14 M071

**Original:** Fig. 6 Design, integration, and application of the WDMS. a Photograph and system block diagram of the WDMS. b–d Real-world outdoor demonstrations of the WDMS under different scenarios: b direct sunlight, c shaded conditions, and d combined photothermal stimulation, benchmarked against commercial sensor references. e Time-resolved light intensity and temperature during shadow–recovery and heating– removal cycles

**中文:** 该段已进入结构化方法步骤；完整逐段翻译待智能体精读补齐。

<a id="M072"></a>
**Source:** p.14 M072

**Original:** https://doi.org/10.1007/s40820-026-02285-7 © The authors

**中文:** 该段已进入结构化方法步骤；完整逐段翻译待智能体精读补齐。

<a id="M073"></a>
**Source:** p.14 M073

**Original:** orthogonality, effectively eliminating crosstalk even within a wide dynamic range of compound environmental stimuli. To further evaluate the system’s robustness under continuous dynamic conditions, we recorded a real-time demonstration covering complete “shadow–recovery” and “heating–removal” cycles (Video S1), with corresponding temporal data presented in Fig. 6e. Throughout the dynamic testing, the system exhibits fast transient response, accurately tracking abrupt optical occlusion and temperature rise events with negligible hysteresis during the subsequent recovery phases. Importantly, the sensing platform maintains strict modal independence: pronounced variations in one environmental parameter produce no measurable

**中文:** 该段已进入结构化方法步骤；完整逐段翻译待智能体精读补齐。

<a id="M074"></a>
**Source:** p.14 M074

**Original:** perturbation in the other. These results confirm that the system achieves real-time, crosstalk-free decoupling even under compound, time-varying environmental stimuli.

**中文:** 该段已进入结构化方法步骤；完整逐段翻译待智能体精读补齐。

<a id="M075"></a>
**Source:** p.14 M075

**Original:** 4 Conclusions

**中文:** 该段已进入结构化方法步骤；完整逐段翻译待智能体精读补齐。

<a id="M076"></a>
**Source:** p.14 M076

**Original:** In this work, we developed a flexible dual-modal sensing transistor (FDST) capable of simultaneously detecting light intensity and temperature within a single sensing unit. By integrating electrospun ZnO nanofibers with an IGZO thinfilm transistor, the device leverages defect-mediated optical excitation and thermally activated interfacial potential

**中文:** 该段已进入结构化方法步骤；完整逐段翻译待智能体精读补齐。

<a id="M077"></a>
**Source:** p.15 M077

**Original:** Nano-Micro Lett. (2026) 18:429 Page 15 of 18 429

**中文:** 该段已进入结构化方法步骤；完整逐段翻译待智能体精读补齐。

<a id="M078"></a>
**Source:** p.15 M078

**Original:** modulation to generate strong photothermal responses. As a result, the FDST achieves a broadband responsivity of up to 2.69 A W−1 and a temperature coefficient of 0.071 °C−1, demonstrating reliable sensitivity to both optical and thermal stimuli. To resolve the intrinsic coupling between these signals, a multibias electrical readout strategy was introduced to encode the stimuli into a bias-dependent current fingerprint. A lightweight MLP was then employed to decode these electrical features, enabling accurate reconstruction of light intensity and temperature with coefficients of determination of 0.992 and 0.989, respectively. Importantly, the FDST exhibits excellent mechanical robustness, maintaining stable sensing performance even after 10,000 bending cycles at a bending radius of 2 mm, highlighting its suitability for flexible and wearable electronics. Furthermore, the device was integrated into a wearable dual-modal monitoring system that enables real-time environmental sensing with negligible modal cross-interference under outdoor conditions. Overall, this work demonstrates a compact device-algorithm co-design strategy for multimodal sensing, providing a scalable pathway toward intelligent wearable perception systems and next-generation electronic skins.

**中文:** 该段已进入结构化方法步骤；完整逐段翻译待智能体精读补齐。

## 图表解读

<a id="F001"></a>
### Fig. 1

**Source:** p.3

![Fig. 1](assets/figure-01.png)

**Original caption:** Fig. 1 Design and implementation of the FDST. a Conceptual illustration of optical and thermal perception from biological systems toward integrated artificial sensing and intelligent applications. b Representative previous single-pixel devices for dual-modal light and temperature sensing based on thermoelectric effects (left, [28–30]) and pyroelectric effects (right, [31]). c This work on a flexible dual-modal sensing transistor for light and temperature sensing

**中文图注:** Fig. 1 原始图注已提取；逐项含义见下方分图说明。

**Reading note:** 重点查看阵列规模、空间分辨率、串扰、读出通道和空间特征表达。

- (a) 重点查看任务设置、基线、消融和失败案例，判断系统演示是否真正支撑前端价值。 原文：Conceptual illustration of optical and thermal perception from biological systems toward integrated artificial sensing and intelligent applications
- (b) 重点查看阵列规模、空间分辨率、串扰、读出通道和空间特征表达。 原文：Representative previous single-pixel devices for dual-modal light and temperature sensing based on thermoelectric effects (left, [28–30]) and pyroelectric effects (right, [31])
- (c) 结合正文首次引用位置和原始图注核对该图的证据角色。 原文：This work on a flexible dual-modal sensing transistor for light and temperature sensing

<a id="F002"></a>
### Fig. 2

**Source:** p.5

![Fig. 2](assets/figure-02.png)

**Original caption:** Fig. 2 Structural architecture and material characterization of the FDST. a Schematic illustration of the FDST structure and layer stack. b Optical microscope image of the electrospun ZnO NFs network. c XRD pattern of the ZnO NFs. d Deconvoluted O 1s XPS spectrum of the ZnO sensing layer. e Depth-dependent O 1s XPS spectra across the ZnO/IGZO stack presented as a waterfall plot. f Deconvoluted O 1s XPS spectrum of the IGZO layer. g Relative content of VO and M–OH as a function of etching time. h UV–Vis absorption spectra of ZnO and IGZO measured over the wavelength range of 250–900 nm after linear background subtraction and normalization. i UPS spectra of the ZnO and IGZO layers

**中文图注:** Fig. 2 原始图注已提取；逐项含义见下方分图说明。

**Reading note:** 重点查看器件结构、材料层次、信号路径和制备流程。

- (a) 重点查看器件结构、材料层次、信号路径和制备流程。 原文：Schematic illustration of the FDST structure and layer stack
- (b) 重点查看阵列规模、空间分辨率、串扰、读出通道和空间特征表达。 原文：Optical microscope image of the electrospun ZnO NFs network
- (c) 结合正文首次引用位置和原始图注核对该图的证据角色。 原文：XRD pattern of the ZnO NFs
- (d) 结合正文首次引用位置和原始图注核对该图的证据角色。 原文：Deconvoluted O 1s XPS spectrum of the ZnO sensing layer
- (e) 结合正文首次引用位置和原始图注核对该图的证据角色。 原文：Depth-dependent O 1s XPS spectra across the ZnO/IGZO stack presented as a waterfall plot
- (f) 结合正文首次引用位置和原始图注核对该图的证据角色。 原文：Deconvoluted O 1s XPS spectrum of the IGZO layer
- (g) 结合正文首次引用位置和原始图注核对该图的证据角色。 原文：Relative content of VO and M–OH as a function of etching time
- (h) 结合正文首次引用位置和原始图注核对该图的证据角色。 原文：UV–Vis absorption spectra of ZnO and IGZO measured over the wavelength range of 250–900 nm after linear background subtraction and normalization
- (i) 结合正文首次引用位置和原始图注核对该图的证据角色。 原文：UPS spectra of the ZnO and IGZO layers

<a id="F003"></a>
### Fig. 3

**Source:** p.7

![Fig. 3](assets/figure-03.png)

**Original caption:** Fig. 3 Optical sensing performance and mechanism of the FDST. a Transfer characteristics measured under different white-light illumination intensities. b Dynamic drain-current response under sequential light-intensity modulation. c Transient drain-current response to a single light on/ off pulse. d Repetitive drain-current response under periodic white-light illumination, with insets showing enlarged cycles. e Schematic of subgap defect excitation and carrier trapping in ZnO under white-light illumination. f FEA-simulated potential distribution in the ZnO/IGZO stack as a function of light intensity. g Benchmark comparison of responsivity versus response time with representative reports

**中文图注:** Fig. 3 原始图注已提取；逐项含义见下方分图说明。

**Reading note:** 重点查看器件结构、材料层次、信号路径和制备流程。

- (a) 结合正文首次引用位置和原始图注核对该图的证据角色。 原文：Transfer characteristics measured under different white-light illumination intensities
- (b) 重点查看标定方法、量程、误差、线性和动态响应，避免只比较单一灵敏度。 原文：Dynamic drain-current response under sequential light-intensity modulation
- (c) 重点查看标定方法、量程、误差、线性和动态响应，避免只比较单一灵敏度。 原文：Transient drain-current response to a single light on/ off pulse
- (d) 重点查看标定方法、量程、误差、线性和动态响应，避免只比较单一灵敏度。 原文：Repetitive drain-current response under periodic white-light illumination, with insets showing enlarged cycles
- (e) 重点查看器件结构、材料层次、信号路径和制备流程。 原文：Schematic of subgap defect excitation and carrier trapping in ZnO under white-light illumination
- (f) 结合正文首次引用位置和原始图注核对该图的证据角色。 原文：FEA-simulated potential distribution in the ZnO/IGZO stack as a function of light intensity
- (g) 重点查看标定方法、量程、误差、线性和动态响应，避免只比较单一灵敏度。 原文：Benchmark comparison of responsivity versus response time with representative reports

<a id="F004"></a>
### Fig. 4

**Source:** p.10

![Fig. 4](assets/figure-04.png)

**Original caption:** Fig. 4 Thermal sensing performance and mechanism of the FDST. a Transfer characteristics measured under different temperatures. b Dynamic drain-current response under sequential temperature steps. c Transient drain-current response to a single-step thermal pulse. d Cycling stability under repeated temperature switching; insets show representative cycles. e Schematic illustration of thermally activated surface processes and capacitive coupling between ZnO and the IGZO channel. f Radar comparison of thermal sensing metrics among representative flexible temperature sensors. g FEA-simulated temperature-dependent potential distribution in the ZnO/IGZO stack

**中文图注:** Fig. 4 原始图注已提取；逐项含义见下方分图说明。

**Reading note:** 重点查看器件结构、材料层次、信号路径和制备流程。

- (a) 结合正文首次引用位置和原始图注核对该图的证据角色。 原文：Transfer characteristics measured under different temperatures
- (b) 重点查看标定方法、量程、误差、线性和动态响应，避免只比较单一灵敏度。 原文：Dynamic drain-current response under sequential temperature steps
- (c) 重点查看标定方法、量程、误差、线性和动态响应，避免只比较单一灵敏度。 原文：Transient drain-current response to a single-step thermal pulse
- (d) 结合正文首次引用位置和原始图注核对该图的证据角色。 原文：Cycling stability under repeated temperature switching; insets show representative cycles
- (e) 重点查看器件结构、材料层次、信号路径和制备流程。 原文：Schematic illustration of thermally activated surface processes and capacitive coupling between ZnO and the IGZO channel
- (f) 结合正文首次引用位置和原始图注核对该图的证据角色。 原文：Radar comparison of thermal sensing metrics among representative flexible temperature sensors
- (g) 结合正文首次引用位置和原始图注核对该图的证据角色。 原文：FEA-simulated temperature-dependent potential distribution in the ZnO/IGZO stack

<a id="F005"></a>
### Fig. 5

**Source:** p.13

![Fig. 5](assets/figure-05.png)

**Original caption:** Fig. 5 Evaluation and implementation of regression models for decoupled light intensity and temperature sensing. a Schematic comparison of regression algorithms, including LR, PR, SVR, XGBoost, and MLP. b R2 for light intensity and temperature prediction across models. c MAE for light intensity and temperature prediction across models. d Architecture of the MLP. e Training loss as a function of epoch for the MLP. f Evolution of R2 during MLP training. g Parity plot of predicted versus true light intensity using the MLP. h Parity plot of predicted versus true temperature using the MLP. i Residual distributions for MLP-based light intensity and temperature predictions

**中文图注:** Fig. 5 原始图注已提取；逐项含义见下方分图说明。

**Reading note:** 重点查看器件结构、材料层次、信号路径和制备流程。

- (a) 重点查看器件结构、材料层次、信号路径和制备流程。 原文：Schematic comparison of regression algorithms, including LR, PR, SVR, XGBoost, and MLP
- (b) 重点查看机制模型与实验结果是否一致，以及关键结构参数的对照关系。 原文：R2 for light intensity and temperature prediction across models
- (c) 重点查看机制模型与实验结果是否一致，以及关键结构参数的对照关系。 原文：MAE for light intensity and temperature prediction across models
- (d) 重点查看器件结构、材料层次、信号路径和制备流程。 原文：Architecture of the MLP
- (e) 结合正文首次引用位置和原始图注核对该图的证据角色。 原文：Training loss as a function of epoch for the MLP
- (f) 结合正文首次引用位置和原始图注核对该图的证据角色。 原文：Evolution of R2 during MLP training
- (g) 结合正文首次引用位置和原始图注核对该图的证据角色。 原文：Parity plot of predicted versus true light intensity using the MLP
- (h) 结合正文首次引用位置和原始图注核对该图的证据角色。 原文：Parity plot of predicted versus true temperature using the MLP
- (i) 结合正文首次引用位置和原始图注核对该图的证据角色。 原文：Residual distributions for MLP-based light intensity and temperature predictions

<a id="F006"></a>
### Fig. 6

**Source:** p.14

![Fig. 6](assets/figure-06.png)

**Original caption:** Fig. 6 Design, integration, and application of the WDMS. a Photograph and system block diagram of the WDMS. b–d Real-world outdoor demonstrations of the WDMS under different scenarios: b direct sunlight, c shaded conditions, and d combined photothermal stimulation, benchmarked against commercial sensor references. e Time-resolved light intensity and temperature during shadow–recovery and heating– removal cycles

**中文图注:** Fig. 6 原始图注已提取；逐项含义见下方分图说明。

**Reading note:** 重点查看任务设置、基线、消融和失败案例，判断系统演示是否真正支撑前端价值。

- (a) 结合正文首次引用位置和原始图注核对该图的证据角色。 原文：Photograph and system block diagram of the WDMS
- (b-d) 结合正文首次引用位置和原始图注核对该图的证据角色。 原文：Real-world outdoor demonstrations of the WDMS under different scenarios: b direct sunlight, c shaded conditions, and d combined photothermal stimulation, benchmarked against commercial sensor references
- (e) 结合正文首次引用位置和原始图注核对该图的证据角色。 原文：Time-resolved light intensity and temperature during shadow–recovery and heating– removal cycles
