# [#HomeBench](https://github.com/BITHLP/HomeBench)

### 📂 Project Files

| File Name | Description |
| :--- | :--- |
| **`context_generator.py`** | LLM API를 사용하여 HomeBench 지시문으로부터 **Core Context(User Story)**와 **Individual Perception**을 자동으로 생성하는 실행 스크립트입니다. |
| **`generated_user_story_perceptions.json`** | LLM을 통해 생성된 최종 결과물로, 가구 전체의 **Core Context**와 각 지시문별 **Perception(상황적 동기)**이 포함되어 있습니다. |
| **`home_status_method_hierarchical.json`** | 가구별(home_id) 방 구성, 기기 목록, 제어 가능한 기능 및 현재 상태가 정의된 **메타데이터**입니다. |
| **`inputs_home40_one.json`** | Home ID 40번에서 발생한 실제 사용자 지시문(Instruction) 리스트로, 컨텍스트 생성의 기초 데이터입니다. |
| **`train_data_part1_converted.json`** | 기존 HomeBench 데이터와 새로 생성된 컨텍스트를 결합하여 모델 학습이 가능하도록 포맷을 변환한 통합 데이터셋입니다. |
