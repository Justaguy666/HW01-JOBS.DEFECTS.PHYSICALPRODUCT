# DEVICE INFO

## Purpose

This file records the physical product selected for Requirement 3 testing.

Goals:

* Identify the exact household device under test
* Preserve required device metadata
* Link the device photo with student ID card evidence
* Support traceability from test cases to the tested product

---

## 1. Device Metadata

| Field | Value |
| --- | --- |
| Device ID | DEV-001 |
| Requirement | R3 |
| Product category | Wireless over-ear headset |
| Brand | BRIDIO / BD-A-B-TH10BRLDL0-BK |
| Model | TH10 |
| Year | 2024 |
| Serial number | Not found |
| Barcode (EAN-13) | 6972706515155 |
| Local product link | https://vn.shp.ee/MMd2R2Qx |

Notes: No dedicated serial number was found on the product packaging. The available SKU/barcode was used for identification purposes.

---

## 2. Public Product Information Used For Test Design

| Field | Source-backed value |
| --- | --- |
| Connection modes | Bluetooth wireless and 3.5 mm AUX wired mode |
| Bluetooth version | V5.3 |
| Battery capacity | 300 mAh |
| Charging time | About 2.5 hours |
| Standby time | About 100 hours |
| Bluetooth range | About 10 m |
| Driver size | 40 mm |
| Frequency range | 20 Hz - 20 kHz |
| Speaker impedance | 32 ohm +/- 15% |
| Speaker sensitivity | 110 dB +/- 3 dB |
| Microphone sensitivity | -42 dB +/- 3 dB |
| Rated input | 5V / 500mA |
| Audio port | AUX / 3.5 mm audio cable |
| Claimed gaming/play time | About 9 hours |
| Listed controls | Play/pause, answer/end call, volume up/down, next/previous, power/pairing, indicator light |
| AUX limitation | Headset buttons do not work when using AUX cable |
| Package contents | Headset, Micro-USB charging cable, 3.5 mm audio cable, user manual |

Notes:

* Public seller listings can be inconsistent. Treat these values as test assumptions until the real device and manual packaging are checked.
* Do not claim official manufacturer certification unless the physical product or official documentation confirms it.

---

## 3. Source Links

| Source | Use | Link |
| --- | --- | --- |
| Shopee BRIDIO TH10 listing | Product identity, seller/warranty context | https://shopee.vn/Tai-Nghe-Bluetooth-Bridio-TH10-Cu%E1%BB%99c-G%E1%BB%8Di-HIFI-Ch%E1%BA%A5t-L%C6%B0%E1%BB%A3ng-%C3%A2m-Thanh-Ch%E1%BA%A5t-L%C6%B0%E1%BB%A3ng-Cao-n%E1%BB%95i-gi%E1%BA%A3m-%E1%BB%93n-tho%E1%BA%A3i-m%C3%A1i-BH-12-th%C3%A1ng-i.1176085600.22890578469 |
| TikTok Shop BRIDIO TH10 listing | Product specifications and package contents | https://shop-vn.tiktok.com/pdp/1730584122605407137 |
| User-provided Shopee short link | Local purchase/reference link | https://vn.shp.ee/MMd2R2Qx |

---

## 4. Physical Evidence

| Evidence Item | Value |
| --- | --- |
| Required photo | `device_photo_with_student_id.jpg` |
| Photo contains device | verified |
| Photo contains student ID card in same frame | verified |
| Anti-cheat status | verified |

---

## 5. Testing Scope

The Requirement 3 test scope covers the BRIDIO TH10 as a physical consumer headset, not only as a Bluetooth device. The scope includes Bluetooth pairing, reconnection, range, audio playback, microphone calls, AUX wired mode, button controls, LED/indicator behavior, charging, battery endurance, thermal safety, foldable hinge durability, headband adjustment, comfort, portability, and realistic household edge cases such as obstruction, noise, low battery, and multi-device connection conflicts.

Out of scope unless extra tools are available:

* Laboratory-grade frequency response measurement
* Precise battery capacity measurement in mAh
* Electrical teardown or internal battery inspection
* Certified acoustic safety measurement

---

## 6. Execution Dataset Summary

| Metric | Value |
| --- | --- |
| Total Requirement 3 test cases | 15 |
| Executed records completed | 15 |
| Passed records | 10 |
| Failed records | 5 |
| Discovered defects | 5 |
| AI-missed edge cases documented | 3 |
| Execution date used in records | 2026-06-01 |

The execution record covers Bluetooth setup, reconnection, range, audio playback, microphone quality, call control, charging, comfort, and hinge-related physical handling for the BRIDIO TH10.

---

## 7. Verification Notes

| Check | Result |
| --- | --- |
| Compared with official R3 requirement | yes |
| Brand/model/year declared | yes |
| Serial number masked | Not found |
| Device photo available | verified |
| Ready for final report | yes |

---

## Final Notes

Requirement 3 now has a complete execution-style dataset for report drafting: 15 test case outcomes, 5 defect records, and traceability across Markdown and workbook artifacts.
