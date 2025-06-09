# NeoShinri MVP – Roadmap (v0.1.0)

This document defines the complete development plan to build the first working MVP of NeoShinri Engine.

## 🎯 Goal

Create a minimal, functional version of NeoShinri capable of processing a single client task end-to-end:
Client → Controller → Tunnel → Agent → Tunnel → Controller → Client.

---

## ✅ Milestone: MVP v0.1.0

### Phase 1: Project Scaffolding

- [x] Create base project structure under `neoshinri/`
- [x] Add `README.md` with MVP goal and structure explanation
- [x] Define `.gitignore`, `requirements.txt`, and minimal `docker-compose.yaml`

### Phase 2: Shared Protocol Definition

- [x] Define `ACPMessage` schema in `shared/protocols/acp.py`
- [x] Define common constants for agent roles and task types

### Phase 3: Controller (Core Brain)

- [ ] Create `controller/main.py` with FastAPI entrypoint
- [ ] Implement basic `Task Planner` (static task generator)
- [ ] Implement `Routing Logic` to dispatch to one predefined agent role
- [ ] Send REST request to Tunnel with structured ACPMessage

### Phase 4: Tunnel (Transport Layer)

- [ ] Create `tunnel/main.py` with FastAPI gateway
- [ ] Implement `ACP Translator` to parse/validate incoming messages
- [ ] Implement `Dispatcher` that routes message to correct Agent REST endpoint
- [ ] Implement mock `Memory Proxy` that returns dummy context

### Phase 5: Agent (Execution Unit)

- [ ] Create basic `agent/basic_agent.py` with `/execute` endpoint
- [ ] Implement simple tool logic (e.g., reverse string or echo input)
- [ ] Print input and return simulated result

### Phase 6: Response Loop

- [ ] Agent returns result → Tunnel → Controller
- [ ] Controller sends unified result back to client

### Phase 7: Testing

- [ ] Create Postman collection or CURL script to simulate task
- [ ] Validate input/output across all layers
- [ ] Add minimal test under `tests/test_roundtrip.py`

### Phase 8: Wrap v0.1.0

- [ ] Tag version v0.1.0 in Git
- [ ] Document endpoint examples in `docs/MVP/API.md`
- [ ] Snapshot architecture diagram as `docs/MVP/architecture-v0.1.0.png`

---

## 🔄 Future Milestones (Post-MVP)

- Add support for multiple agents
- Integrate Long-Term Memory
- Add Kafka-based async support
- Implement Agent Registry and Health checks
- Add Observability stack
