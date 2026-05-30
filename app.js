/**
 * ==========================================================================
 * AEGIS GRC - GOVERNANCE, RISK, AND COMPLIANCE OPERATIONS ENGINE
 * Enterprise IRM System of Record - Continuous Compliance Architecture
 * ==========================================================================
 */

// --- BASE DATA SCHEMA (10 ISO 27001 Controls & 8 ISO 27701 Controls) ---
const DEFAULT_GRC_CONTROLS = [
    // ISO 27001 Controls (Information Security Management System - ISMS)
    {
        id: "A.5",
        name: "Organizational Policies",
        objective: "Establish formal directives and governance frameworks for information security operations.",
        framework: "ISO-27001",
        state: "Monitoring",
        status: "PASSED",
        owner: "CISO",
        frequency: "Annually",
        evidenceSource: "Google Workspace Compliance Drive",
        inherentRisk: "High",
        notes: "Corporate Security Policies v4.2 approved by Board of Directors. Policy distribution list verified via Okta groups.",
        lastReviewed: "2026-05-10"
    },
    {
        id: "A.6",
        name: "Human Resource Security",
        objective: "Ensure that employees understand their responsibilities and are suitable for their roles.",
        framework: "ISO-27001",
        state: "Monitoring",
        status: "WARNING",
        owner: "HR Director",
        frequency: "Continuous (Automated)",
        evidenceSource: "Checkr API Integration",
        inherentRisk: "Medium",
        notes: "Background checks active. Mandatory security onboarding completed for 89% of employees. Reminders sent to pending.",
        lastReviewed: "2026-05-18"
    },
    {
        id: "A.7",
        name: "Physical & Environmental Security",
        objective: "Prevent unauthorized physical access, damage, or disruption to offices and server systems.",
        framework: "ISO-27001",
        state: "Monitoring",
        status: "PASSED",
        owner: "IT Security Lead",
        frequency: "Quarterly",
        evidenceSource: "Brivo Badge Access System",
        inherentRisk: "Medium",
        notes: "Office badge access reader registers audited. Server facility climate controls telemetry synced with GRC panel.",
        lastReviewed: "2026-04-20"
    },
    {
        id: "A.8",
        name: "Asset Management",
        objective: "Identify corporate data/hardware assets and define appropriate lifecycle protection policies.",
        framework: "ISO-27001",
        state: "Monitoring",
        status: "PASSED",
        owner: "IT Manager",
        frequency: "Continuous (Automated)",
        evidenceSource: "AWS Config Inventory",
        inherentRisk: "High",
        notes: "Hardware asset registry automated via AWS System Manager. Software license inventory audited and active.",
        lastReviewed: "2026-05-22"
    },
    {
        id: "A.9",
        name: "Access Control",
        objective: "Restrict system and data access based on strict business roles and need-to-know constraints.",
        framework: "ISO-27001",
        state: "Under Review",
        status: "WARNING",
        owner: "IT Security Lead",
        frequency: "Continuous (Automated)",
        evidenceSource: "Okta API Integration",
        inherentRisk: "Critical",
        notes: "Multi-Factor Authentication (MFA) active. Quarterly review identified 5 stale service account exemptions to clear.",
        lastReviewed: "2026-05-01"
    },
    {
        id: "A.10",
        name: "Cryptography",
        objective: "Implement proper encryption standards to protect data confidentiality, integrity, and transit security.",
        framework: "ISO-27001",
        state: "Monitoring",
        status: "PASSED",
        owner: "IT Security Lead",
        frequency: "Continuous (Automated)",
        evidenceSource: "AWS KMS Telemetry",
        inherentRisk: "Critical",
        notes: "AES-256 enforced at rest. TLS 1.3 mandated for API gateways. Automated key rotation checked weekly via AWS KMS.",
        lastReviewed: "2026-05-14"
    },
    {
        id: "A.12",
        name: "Operations Security",
        objective: "Ensure secure and stable operations of facilities, backup integrity, and malware defenses.",
        framework: "ISO-27001",
        state: "Under Review",
        status: "FAILED",
        owner: "IT Manager",
        frequency: "Quarterly",
        evidenceSource: "AWS Backup Audit Logs",
        inherentRisk: "Critical",
        notes: "Automated database backups running successfully. However, the annual backup restoration drill script timed out.",
        lastReviewed: "2026-03-12"
    },
    {
        id: "A.13",
        name: "Communications Security",
        objective: "Ensure network boundary security, transmission isolation, and firewall containment.",
        framework: "ISO-27001",
        state: "Monitoring",
        status: "PASSED",
        owner: "IT Security Lead",
        frequency: "Continuous (Automated)",
        evidenceSource: "Palo Alto Firewall Logs",
        inherentRisk: "High",
        notes: "Zero-trust network architecture active. Production database environments segregated into private subnets.",
        lastReviewed: "2026-05-25"
    },
    {
        id: "A.14",
        name: "System Acquisition & Development",
        objective: "Integrate security guidelines throughout the entire Software Development Lifecycle (SDLC).",
        framework: "ISO-27001",
        state: "Draft",
        status: "FAILED",
        owner: "IT Manager",
        frequency: "Quarterly",
        evidenceSource: "GitHub API Integration",
        inherentRisk: "High",
        notes: "SAST scanning integrated in CI/CD pipeline, but legacy software system security assessment criteria is missing.",
        lastReviewed: "2026-02-18"
    },
    {
        id: "A.16",
        name: "Incident Management",
        objective: "Establish structural incident response boundaries, playbook protocols, and audit records.",
        framework: "ISO-27001",
        state: "Monitoring",
        status: "WARNING",
        owner: "CISO",
        frequency: "Annually",
        evidenceSource: "PagerDuty System Logs",
        inherentRisk: "High",
        notes: "Incident Response Playbook is operational. Mock tabletop drill completed; awaiting post-mortem reporting templates.",
        lastReviewed: "2026-05-08"
    },

    // ISO 27701 Privacy Controls (Privacy Information Management System - PIMS)
    {
        id: "5.2",
        name: "PIMS Policies",
        objective: "Align organization directives with privacy frameworks and legal requirements for processing PII.",
        framework: "ISO-27701",
        state: "Monitoring",
        status: "PASSED",
        owner: "Legal Lead",
        frequency: "Annually",
        evidenceSource: "Google Workspace Compliance Drive",
        inherentRisk: "High",
        notes: "PIMS Privacy Policy Annex drafted, reviewed by DPO, and approved by executive board. Intranet updated.",
        lastReviewed: "2026-05-11"
    },
    {
        id: "6.3",
        name: "Privacy Roles & Responsibilities",
        objective: "Establish formal corporate responsibilities for privacy compliance, specifically appointing a DPO.",
        framework: "ISO-27701",
        state: "Monitoring",
        status: "PASSED",
        owner: "DPO",
        frequency: "Annually",
        evidenceSource: "ServiceNow Org Chart",
        inherentRisk: "Medium",
        notes: "Data Protection Officer (DPO) formally appointed and registered with regulatory authorities.",
        lastReviewed: "2026-05-09"
    },
    {
        id: "7.2",
        name: "Conditions for Collection",
        objective: "Ensure explicit legal consent mechanisms and clear data collection boundaries are active.",
        framework: "ISO-27701",
        state: "Under Review",
        status: "WARNING",
        owner: "DPO",
        frequency: "Quarterly",
        evidenceSource: "OneTrust Consent SDK",
        inherentRisk: "High",
        notes: "Explicit consent records stored on sign-up, but historical marketing email lists require consent validation.",
        lastReviewed: "2026-05-02"
    },
    {
        id: "7.3",
        name: "Obligations to PII Principals",
        objective: "Provide automated access, deletion, and export mechanisms for data subject rights (DSAR).",
        framework: "ISO-27701",
        state: "Draft",
        status: "FAILED",
        owner: "DPO",
        frequency: "Continuous (Automated)",
        evidenceSource: "Okta Customer Registry",
        inherentRisk: "Critical",
        notes: "DSAR compliance portal is currently in development. Client deletion scripts are still executed manually.",
        lastReviewed: "2026-03-30"
    },
    {
        id: "7.4",
        name: "Privacy Notice",
        objective: "Ensure clear, transparent, and accurate privacy disclosures are published on corporate front-ends.",
        framework: "ISO-27701",
        state: "Monitoring",
        status: "PASSED",
        owner: "Legal Lead",
        frequency: "Annually",
        evidenceSource: "Web Server Crawler Sync",
        inherentRisk: "High",
        notes: "Privacy notice updated and published. Maps to GDPR, CCPA, and global privacy standard changes.",
        lastReviewed: "2026-05-24"
    },
    {
        id: "7.5",
        name: "Providing Access to PII",
        objective: "Implement secure and verified data export utilities for customer record retrieval.",
        framework: "ISO-27701",
        state: "Monitoring",
        status: "WARNING",
        owner: "IT Security Lead",
        frequency: "Quarterly",
        evidenceSource: "OneTrust Portal",
        inherentRisk: "Medium",
        notes: "Support verification scripts active. Customer PII exporter tool has pending security verification.",
        lastReviewed: "2026-05-19"
    },
    {
        id: "8.2",
        name: "Conditions for Processing",
        objective: "Enforce contract boundaries, data mapping, and subcontractor agreements (DPA).",
        framework: "ISO-27701",
        state: "Monitoring",
        status: "PASSED",
        owner: "Legal Lead",
        frequency: "Annually",
        evidenceSource: "DocuSign GRC Library",
        inherentRisk: "High",
        notes: "Data Processing Addendums (DPA) reviewed and signed for all active third-party subprocessors.",
        lastReviewed: "2026-05-21"
    },
    {
        id: "8.5",
        name: "Data Transfer Accountability",
        objective: "Verify legal standards and region parameters before transferring customer PII across borders.",
        framework: "ISO-27701",
        state: "Monitoring",
        status: "EXEMPT",
        owner: "DPO",
        frequency: "Continuous (Automated)",
        evidenceSource: "AWS VPC Flow Logs Check",
        inherentRisk: "Low",
        notes: "No cross-border transfers permitted. Telemetry shows all databases isolated inside national data centers.",
        lastReviewed: "2026-05-30"
    }
];

// --- APP STATE ---
let state = {
    controls: [],
    activeFramework: "ISO-27001",
    searchQuery: "",
    activeHeatmapFilter: null,
    expandedControlId: null
};

// --- DOM ELEMENTS ---
const elements = {
    metricCompliancePct: document.getElementById("metric-compliance-pct"),
    metricActiveControls: document.getElementById("metric-active-controls"),
    metricResidualRisk: document.getElementById("metric-residual-risk"),
    metricOpenGaps: document.getElementById("metric-open-gaps"),
    tabIso27001: document.getElementById("tab-iso27001"),
    tabIso27701: document.getElementById("tab-iso27701"),
    grcSearch: document.getElementById("grc-search"),
    filterBanner: document.getElementById("filter-banner"),
    filterBannerText: document.getElementById("filter-banner-text"),
    filterClearBtn: document.getElementById("filter-clear-btn"),
    grcControlsContainer: document.getElementById("grc-controls-container"),
    sidebarProgressTitle: document.getElementById("sidebar-progress-title"),
    progressCircle: document.getElementById("progress-circle"),
    frameworkPercent: document.getElementById("framework-percent"),
    heatmapGridContainer: document.getElementById("heatmap-grid-container"),
    sidebarGapsContainer: document.getElementById("sidebar-gaps-container"),
    btnExportCsv: document.getElementById("btn-export-csv"),
    btnTriggerSync: document.getElementById("btn-trigger-sync"),
    toastElement: document.getElementById("grc-toast"),
    toastTitle: document.getElementById("toast-title"),
    toastMessage: document.getElementById("toast-message"),
    countMonitoring: document.getElementById("count-state-monitoring"),
    countReview: document.getElementById("count-state-review"),
    countDraft: document.getElementById("count-state-draft"),
    countRetired: document.getElementById("count-state-retired")
};

// --- INITIALIZATION ---
function init() {
    // 1. Load data from LocalStorage
    const saved = localStorage.getItem("aegis_grc_controls_storage");
    if (saved) {
        try {
            state.controls = JSON.parse(saved);
        } catch (e) {
            console.error("Error parsing GRC database state, restoring defaults.", e);
            state.controls = JSON.parse(JSON.stringify(DEFAULT_GRC_CONTROLS));
        }
    } else {
        state.controls = JSON.parse(JSON.stringify(DEFAULT_GRC_CONTROLS));
    }

    setupEventListeners();
    render();
}

// --- EVENT LISTENERS ---
function setupEventListeners() {
    // Bootstrap Tabs selection
    elements.tabIso27001.addEventListener("click", () => switchFramework("ISO-27001"));
    elements.tabIso27701.addEventListener("click", () => switchFramework("ISO-27701"));

    // Search Query input
    elements.grcSearch.addEventListener("input", (e) => {
        state.searchQuery = e.target.value.toLowerCase().trim();
        renderControlsList();
    });

    // Reset view banner action
    elements.filterClearBtn.addEventListener("click", resetAllFilters);

    // CSV Exporter
    elements.btnExportCsv.addEventListener("click", exportAuditLedger);

    // Global Integration Sync Simulator
    elements.btnTriggerSync.addEventListener("click", runIntegrationsAutomatedSync);

    // Heatmap Matrix cell filter actions
    const cells = elements.heatmapGridContainer.querySelectorAll(".heatmap-cell-grc");
    cells.forEach(cell => {
        cell.addEventListener("click", () => {
            const row = cell.dataset.row;
            const col = cell.dataset.col;
            toggleHeatmapFilter(row, col);
        });
    });
}

// --- STATE MANAGEMENT ---
function switchFramework(framework) {
    if (state.activeFramework === framework) return;

    state.activeFramework = framework;
    state.activeHeatmapFilter = null;
    state.expandedControlId = null;

    elements.tabIso27001.classList.toggle("active", framework === "ISO-27001");
    elements.tabIso27701.classList.toggle("active", framework === "ISO-27701");

    render();
}

function updateControlField(controlId, fieldName, value) {
    const control = state.controls.find(c => c.id === controlId);
    if (!control) return;

    control[fieldName] = value;
    saveState();

    // Trigger instant statistics refresh
    updateKPIs();
    updateSidebarProgress();
    updateHeatmapMatrix();
    updateRemediationQueue();
    updateLifecycleCounts();
}

function saveState() {
    localStorage.setItem("aegis_grc_controls_storage", JSON.stringify(state.controls));
}

function toggleHeatmapFilter(row, col) {
    if (state.activeHeatmapFilter && state.activeHeatmapFilter.row === row && state.activeHeatmapFilter.col === col) {
        state.activeHeatmapFilter = null;
    } else {
        state.activeHeatmapFilter = { row, col };
    }
    
    renderHeatmapSelection();
    renderControlsList();
}

function resetAllFilters() {
    state.searchQuery = "";
    state.activeHeatmapFilter = null;
    elements.grcSearch.value = "";

    renderHeatmapSelection();
    renderControlsList();
}

// --- AUDIT MATHEMATICS & CALCULATIONS ---

/**
 * Standard GRC Mitigated Risk Model
 * Calculates residual risk by lowering inherent threats if compliance is passed.
 */
function getResidualRisk(inherent, status) {
    if (status === "PASSED" || status === "EXEMPT") {
        if (inherent === "Critical") return "Medium";
        if (inherent === "High") return "Low";
        return "Low";
    } else if (status === "WARNING") {
        if (inherent === "Critical") return "High";
        if (inherent === "High") return "Medium";
        return "Low";
    }
    // FAILED: Residual risk equals Inherent
    return inherent;
}

function mapControlToHeatmapCell(control) {
    // Likelihood Map (Control Health):
    // FAILED -> High Likelihood of risk
    // WARNING -> Med Likelihood
    // PASSED / EXEMPT -> Low Likelihood
    let row = "Low";
    if (control.status === "FAILED") row = "High";
    else if (control.status === "WARNING") row = "Med";

    // Impact Map (Inherent Risk):
    // Critical / High -> High Impact
    // Medium -> Med Impact
    // Low -> Low Impact
    let col = "Low";
    if (control.inherentRisk === "Critical" || control.inherentRisk === "High") col = "High";
    else if (control.inherentRisk === "Medium") col = "Med";

    return { row, col };
}

// --- RENDER ENGINE ---
function render() {
    updateKPIs();
    renderControlsList();
    updateSidebarProgress();
    updateHeatmapMatrix();
    updateRemediationQueue();
    updateLifecycleCounts();
}

function updateKPIs() {
    // 1. Overall Compliance Rate (PASSED = 100%, WARNING = 50%, FAILED = 0%, EXEMPT = excluded)
    const applicable = state.controls.filter(c => c.status !== "EXEMPT");
    let totalScore = 0;

    applicable.forEach(c => {
        if (c.status === "PASSED") totalScore += 100;
        else if (c.status === "WARNING") totalScore += 50;
    });

    const pct = applicable.length > 0 ? Math.round(totalScore / applicable.length) : 100;
    elements.metricCompliancePct.innerText = `${pct}%`;

    // 2. Active Controls
    const currentScope = state.controls.filter(c => c.framework === state.activeFramework);
    elements.metricActiveControls.innerText = currentScope.length;

    // 3. Open Remediation Gaps (FAILED controls count)
    const failedCount = state.controls.filter(c => c.status === "FAILED").length;
    elements.metricOpenGaps.innerText = failedCount;

    // 4. Overall Residual Risk Exposure Rating
    const highRisks = state.controls.filter(c => {
        const resRisk = getResidualRisk(c.inherentRisk, c.status);
        return resRisk === "Critical" || resRisk === "High";
    }).length;

    if (highRisks > 2) {
        elements.metricResidualRisk.innerText = "HIGH EXPOSURE";
        elements.metricResidualRisk.style.color = "var(--risk-critical)";
    } else if (highRisks > 0) {
        elements.metricResidualRisk.innerText = "MODERATE RISK";
        elements.metricResidualRisk.style.color = "var(--risk-high)";
    } else {
        elements.metricResidualRisk.innerText = "MINIMAL / CONTROLLED";
        elements.metricResidualRisk.style.color = "var(--color-passed)";
    }
}

function renderControlsList() {
    elements.grcControlsContainer.innerHTML = "";

    // 1. Filter by Active Framework
    let list = state.controls.filter(c => c.framework === state.activeFramework);

    // 2. Search query filter
    if (state.searchQuery) {
        list = list.filter(c => 
            c.id.toLowerCase().includes(state.searchQuery) ||
            c.name.toLowerCase().includes(state.searchQuery) ||
            c.objective.toLowerCase().includes(state.searchQuery) ||
            c.notes.toLowerCase().includes(state.searchQuery)
        );
    }

    // 3. Heatmap matrix filter
    if (state.activeHeatmapFilter) {
        list = list.filter(c => {
            const cell = mapControlToHeatmapCell(c);
            return cell.row === state.activeHeatmapFilter.row && cell.col === state.activeHeatmapFilter.col;
        });
    }

    // Toggle Filters Banner
    if (state.searchQuery || state.activeHeatmapFilter) {
        elements.filterBanner.style.display = "block";
        let bannerText = "Active GRC Filter: ";
        if (state.searchQuery) bannerText += `Query matching "${state.searchQuery}" `;
        if (state.activeHeatmapFilter) {
            bannerText += `${state.activeHeatmapFilter.row} Likelihood / ${state.activeHeatmapFilter.col} Impact `;
        }
        elements.filterBannerText.innerText = `${bannerText}(${list.length} controls separated)`;
    } else {
        elements.filterBanner.style.display = "none";
    }

    if (list.length === 0) {
        elements.grcControlsContainer.innerHTML = `
            <tr>
                <td colspan="5" class="text-center py-5 text-muted">
                    <svg width="32" height="32" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round" class="opacity-50 mb-2"><circle cx="11" cy="11" r="8"></circle><line x1="21" y1="21" x2="16.65" y2="16.65"></line></svg>
                    <p class="small mb-0">No active control objectives match the isolated audit filter.</p>
                </td>
            </tr>
        `;
        return;
    }

    // Render Table Rows
    list.forEach(control => {
        const trMain = document.createElement("tr");
        trMain.className = "table-row-grc";
        if (state.expandedControlId === control.id) {
            trMain.classList.add("active-expand");
        }

        const residual = getResidualRisk(control.inherentRisk, control.status);

        trMain.innerHTML = `
            <td>
                <div class="d-flex align-items-center gap-2 mb-1">
                    <span class="control-id-tag">${control.id}</span>
                    <span class="control-title">${control.name}</span>
                </div>
                <div class="control-desc" title="${control.objective}">${control.objective}</div>
            </td>
            <td>
                <span class="badge-owner d-block text-center mb-1">${control.owner}</span>
                <span class="d-block text-center text-muted" style="font-size:0.62rem;">${control.frequency}</span>
            </td>
            <td>
                <div class="integration-tag mb-1">${control.evidenceSource}</div>
                <div class="text-muted" style="font-size:0.62rem;">Assurance Monitoring Active</div>
            </td>
            <td>
                <span class="badge-compliance ${getComplianceBadgeClass(control.status)}">
                    ${control.status}
                </span>
            </td>
            <td>
                <div class="d-flex align-items-center justify-content-center gap-1">
                    <span class="badge-risk ${getRiskBadgeClass(control.inherentRisk)}">${control.inherentRisk}</span>
                    <span class="text-muted" style="font-size:0.6rem;">➔</span>
                    <span class="badge-risk ${getRiskBadgeClass(residual)}">${residual}</span>
                </div>
            </td>
        `;

        // Collapsible Drawer Row
        const trDrawer = document.createElement("tr");
        trDrawer.className = "grc-drawer-row";
        trDrawer.style.display = state.expandedControlId === control.id ? "table-row" : "none";
        
        trDrawer.innerHTML = `
            <td colspan="5">
                <div class="grc-drawer-inner">
                    <div class="drawer-remediation-notes">
                        <label>Audited System Evidence & Remediation Progress Logs</label>
                        <textarea class="form-control form-control-grc notes-textarea-grc w-100 flex-grow-1" placeholder="Add specific server configurations, audit credentials, or remediation steps...">${control.notes}</textarea>
                    </div>
                    
                    <div class="d-flex flex-column justify-content-between">
                        <div class="row g-2 mb-3">
                            <div class="col-6">
                                <label class="d-block mb-1" style="font-size:0.65rem; color:var(--text-muted); font-weight:700; text-transform:uppercase;">Control Owner</label>
                                <select class="form-select form-select-grc select-owner">
                                    <option value="CISO" ${control.owner === "CISO" ? "selected" : ""}>CISO</option>
                                    <option value="DPO" ${control.owner === "DPO" ? "selected" : ""}>DPO</option>
                                    <option value="IT Security Lead" ${control.owner === "IT Security Lead" ? "selected" : ""}>IT Security Lead</option>
                                    <option value="IT Manager" ${control.owner === "IT Manager" ? "selected" : ""}>IT Manager</option>
                                    <option value="HR Director" ${control.owner === "HR Director" ? "selected" : ""}>HR Director</option>
                                    <option value="Legal Lead" ${control.owner === "Legal Lead" ? "selected" : ""}>Legal Lead</option>
                                </select>
                            </div>
                            <div class="col-6">
                                <label class="d-block mb-1" style="font-size:0.65rem; color:var(--text-muted); font-weight:700; text-transform:uppercase;">Lifecycle State</label>
                                <select class="form-select form-select-grc select-state">
                                    <option value="Monitoring" ${control.state === "Monitoring" ? "selected" : ""}>Monitoring</option>
                                    <option value="Under Review" ${control.state === "Under Review" ? "selected" : ""}>Under Review</option>
                                    <option value="Draft" ${control.state === "Draft" ? "selected" : ""}>Draft</option>
                                    <option value="Retired" ${control.state === "Retired" ? "selected" : ""}>Retired</option>
                                </select>
                            </div>
                            <div class="col-6">
                                <label class="d-block mb-1" style="font-size:0.65rem; color:var(--text-muted); font-weight:700; text-transform:uppercase;">Inherent Risk</label>
                                <select class="form-select form-select-grc select-inherent">
                                    <option value="Critical" ${control.inherentRisk === "Critical" ? "selected" : ""}>Critical</option>
                                    <option value="High" ${control.inherentRisk === "High" ? "selected" : ""}>High</option>
                                    <option value="Medium" ${control.inherentRisk === "Medium" ? "selected" : ""}>Medium</option>
                                    <option value="Low" ${control.inherentRisk === "Low" ? "selected" : ""}>Low</option>
                                </select>
                            </div>
                            <div class="col-6">
                                <label class="d-block mb-1" style="font-size:0.65rem; color:var(--text-muted); font-weight:700; text-transform:uppercase;">Assurance Status</label>
                                <select class="form-select form-select-grc select-status">
                                    <option value="PASSED" ${control.status === "PASSED" ? "selected" : ""}>PASSED (Compliant)</option>
                                    <option value="WARNING" ${control.status === "WARNING" ? "selected" : ""}>WARNING (Partial)</option>
                                    <option value="FAILED" ${control.status === "FAILED" ? "selected" : ""}>FAILED (Gap)</option>
                                    <option value="EXEMPT" ${control.status === "EXEMPT" ? "selected" : ""}>EXEMPT (Exempt)</option>
                                </select>
                            </div>
                            <div class="col-6">
                                <label class="d-block mb-1" style="font-size:0.65rem; color:var(--text-muted); font-weight:700; text-transform:uppercase;">Test Frequency</label>
                                <select class="form-select form-select-grc select-frequency">
                                    <option value="Continuous (Automated)" ${control.frequency === "Continuous (Automated)" ? "selected" : ""}>Continuous (Automated)</option>
                                    <option value="Quarterly" ${control.frequency === "Quarterly" ? "selected" : ""}>Quarterly</option>
                                    <option value="Annually" ${control.frequency === "Annually" ? "selected" : ""}>Annually</option>
                                </select>
                            </div>
                            <div class="col-6">
                                <label class="d-block mb-1" style="font-size:0.65rem; color:var(--text-muted); font-weight:700; text-transform:uppercase;">Last Review</label>
                                <input type="date" class="form-control form-control-grc date-reviewed" value="${control.lastReviewed}">
                            </div>
                        </div>

                        <div class="d-flex gap-2 justify-content-end pt-2">
                            <button class="btn btn-secondary-grc btn-run-test px-3 d-flex align-items-center gap-1" style="font-size: 0.72rem !important; border-color: rgba(16, 185, 129, 0.3) !important; color: var(--color-passed) !important;">
                                ⚡ Test Scan
                            </button>
                            <button class="btn btn-secondary-grc btn-assign px-3 d-flex align-items-center gap-1" style="font-size: 0.72rem !important;">
                                👤 Assign Task
                            </button>
                        </div>
                    </div>
                </div>
            </td>
        `;

        // Toggling Row Expand Expand
        trMain.addEventListener("click", (e) => {
            // Avoid expanding if select dropdowns or buttons clicked inside
            if (e.target.closest("select") || e.target.closest("button") || e.target.closest("textarea")) {
                return;
            }

            if (state.expandedControlId === control.id) {
                state.expandedControlId = null;
            } else {
                state.expandedControlId = control.id;
            }
            renderControlsList();
        });

        // Set inputs events inside drawer
        if (state.expandedControlId === control.id) {
            const drawerInner = trDrawer.querySelector(".grc-drawer-inner");
            
            // Notes area
            drawerInner.querySelector(".notes-textarea-grc").addEventListener("input", (e) => {
                updateControlField(control.id, "notes", e.target.value);
            });

            // Owner
            drawerInner.querySelector(".select-owner").addEventListener("change", (e) => {
                updateControlField(control.id, "owner", e.target.value);
            });

            // GRC State
            drawerInner.querySelector(".select-state").addEventListener("change", (e) => {
                updateControlField(control.id, "state", e.target.value);
            });

            // Inherent Risk
            drawerInner.querySelector(".select-inherent").addEventListener("change", (e) => {
                updateControlField(control.id, "inherentRisk", e.target.value);
            });

            // GRC Status
            drawerInner.querySelector(".select-status").addEventListener("change", (e) => {
                updateControlField(control.id, "status", e.target.value);
            });

            // Frequency
            drawerInner.querySelector(".select-frequency").addEventListener("change", (e) => {
                updateControlField(control.id, "frequency", e.target.value);
            });

            // Review Date
            drawerInner.querySelector(".date-reviewed").addEventListener("change", (e) => {
                updateControlField(control.id, "lastReviewed", e.target.value);
            });

            // Run automated single test scan
            drawerInner.querySelector(".btn-run-test").addEventListener("click", () => {
                showToast(`Initiating local automated test for objective ${control.id} via ${control.evidenceSource}...`);
                const testBtn = drawerInner.querySelector(".btn-run-test");
                testBtn.innerText = "⏳ Scanning...";
                testBtn.disabled = true;

                setTimeout(() => {
                    testBtn.innerText = "⚡ Test Scan";
                    testBtn.disabled = false;
                    updateControlField(control.id, "status", "PASSED");
                    showToast(`API Integration check PASSED: Evidence successfully uploaded for ${control.id}!`, "Success");
                    render();
                }, 900);
            });

            // Assign Remediation Task
            drawerInner.querySelector(".btn-assign").addEventListener("click", () => {
                showToast(`Remediation ticket generated successfully! Assigned directly to: ${control.owner}.`);
            });
        }

        elements.grcControlsContainer.appendChild(trMain);
        elements.grcControlsContainer.appendChild(trDrawer);
    });
}

function getComplianceBadgeClass(status) {
    switch (status) {
        case "PASSED": return "badge-passed";
        case "WARNING": return "badge-warning";
        case "FAILED": return "badge-failed";
        case "EXEMPT": return "badge-exempt";
        default: return "";
    }
}

function getRiskBadgeClass(risk) {
    switch (risk) {
        case "Critical": return "badge-risk-crit";
        case "High": return "badge-risk-hi";
        case "Medium": return "badge-risk-med";
        case "Low": return "badge-risk-lo";
        default: return "";
    }
}

// --- SIDEBAR COMPLIANCE PROGRESS RING ---
function updateSidebarProgress() {
    const list = state.controls.filter(c => c.framework === state.activeFramework);
    const titleText = state.activeFramework === "ISO-27001" ? "ISO 27001 ISMS Progress" : "ISO 27701 PIMS Progress";
    elements.sidebarProgressTitle.innerHTML = `<span>${titleText}</span>`;

    const applicable = list.filter(c => c.status !== "EXEMPT");
    if (applicable.length === 0) {
        setSVGProgress(100);
        return;
    }

    let score = 0;
    applicable.forEach(c => {
        if (c.status === "PASSED") score += 100;
        else if (c.status === "WARNING") score += 50;
    });

    const percent = Math.round(score / applicable.length);
    setSVGProgress(percent);
}

function setSVGProgress(percent) {
    elements.frameworkPercent.innerText = `${percent}%`;
    const r = 48;
    const circ = 2 * Math.PI * r; // 301.59
    const offset = circ - (percent / 100) * circ;
    elements.progressCircle.style.strokeDashoffset = offset;
}

// --- SIDEBAR HEATMAP CALCULATION MATRIX ---
function updateHeatmapMatrix() {
    const matrix = {
        High: { Low: 0, Med: 0, High: 0 },
        Med:  { Low: 0, Med: 0, High: 0 },
        Low:  { Low: 0, Med: 0, High: 0 }
    };

    // Calculate distributions across ALL controls in registry
    state.controls.forEach(c => {
        const cell = mapControlToHeatmapCell(c);
        if (cell) {
            matrix[cell.row][cell.col]++;
        }
    });

    // Populate matrix GUI
    for (let r in matrix) {
        for (let c in matrix[r]) {
            const count = matrix[r][c];
            const cellId = `cell-${r.toLowerCase()}-${c.toLowerCase().substring(0,3)}`;
            const cellElem = document.getElementById(cellId);
            if (cellElem) {
                const counter = cellElem.querySelector(".heatmap-count");
                if (counter) counter.innerText = count;

                if (count > 0) {
                    cellElem.style.opacity = "1";
                    cellElem.style.fontWeight = "800";
                } else {
                    cellElem.style.opacity = "0.35";
                    cellElem.style.fontWeight = "500";
                }
            }
        }
    }
}

function renderHeatmapSelection() {
    const cells = elements.heatmapGridContainer.querySelectorAll(".heatmap-cell-grc");
    cells.forEach(cell => {
        const r = cell.dataset.row;
        const c = cell.dataset.col;
        const active = state.activeHeatmapFilter && state.activeHeatmapFilter.row === r && state.activeHeatmapFilter.col === c;
        cell.classList.toggle("active-filter", !!active);
    });
}

// --- SIDEBAR LIFECYCLE METRICS ---
function updateLifecycleCounts() {
    const counts = { Monitoring: 0, "Under Review": 0, Draft: 0, Retired: 0 };
    
    state.controls.forEach(c => {
        if (counts[c.state] !== undefined) {
            counts[c.state]++;
        }
    });

    elements.countMonitoring.innerText = counts["Monitoring"];
    elements.countReview.innerText = counts["Under Review"];
    elements.countDraft.innerText = counts["Draft"];
    elements.countRetired.innerText = counts["Retired"];
}

// --- SIDEBAR REMEDIATION QUEUE (GAPS) ---
function updateRemediationQueue() {
    elements.sidebarGapsContainer.innerHTML = "";

    // Gather failed controls
    let gaps = state.controls.filter(c => c.status === "FAILED");

    // Sort by Inherent Risk severity: Critical (4) > High (3) > Medium (2) > Low (1)
    const weights = { Critical: 4, High: 3, Medium: 2, Low: 1 };
    gaps.sort((a, b) => {
        const wA = weights[a.inherentRisk] || 0;
        const wB = weights[b.inherentRisk] || 0;
        if (wB !== wA) return wB - wA;
        return a.id.localeCompare(b.id);
    });

    const topGaps = gaps.slice(0, 3);

    if (topGaps.length === 0) {
        elements.sidebarGapsContainer.innerHTML = `
            <div class="text-center text-muted py-3" style="font-size:0.75rem;">
                <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" class="text-success mb-1 d-block mx-auto"><path d="M22 11.08V12a10 10 0 1 1-5.93-9.14"></path><polyline points="22 4 12 14.01 9 11.01"></polyline></svg>
                <span>No remediation gaps! Base controls fully approved.</span>
            </div>
        `;
        return;
    }

    topGaps.forEach(gap => {
        const gapDiv = document.createElement("div");
        gapDiv.className = "gap-row-grc d-flex justify-content-between align-items-center";

        gapDiv.innerHTML = `
            <div class="sidebar-gap-meta min-w-0">
                <div class="d-flex align-items-center gap-2 mb-1">
                    <span class="gap-id-tag" style="font-size:0.65rem;">${gap.framework === "ISO-27001" ? "ISO 27001" : "ISO 27701"} • ${gap.id}</span>
                    <span class="badge-risk ${getRiskBadgeClass(gap.inherentRisk)}" style="font-size:0.5rem !important; padding: 0.05rem 0.25rem !important;">${gap.inherentRisk}</span>
                </div>
                <div class="gap-name-text" title="${gap.name}" style="font-size:0.78rem; font-weight:600; color:#fff; white-space:nowrap; overflow:hidden; text-overflow:ellipsis;">${gap.name}</div>
            </div>
            <button class="btn btn-secondary-grc py-1 px-2 d-flex align-items-center justify-content-center btn-gap-jump" title="Isolate and expand this control row">
                ➔
            </button>
        `;

        gapDiv.querySelector(".btn-gap-jump").addEventListener("click", () => {
            jumpToControlObjective(gap.framework, gap.id);
        });

        elements.sidebarGapsContainer.appendChild(gapDiv);
    });
}

function jumpToControlObjective(framework, controlId) {
    if (state.activeFramework !== framework) {
        switchFramework(framework);
    }

    if (state.activeHeatmapFilter) {
        resetAllFilters();
    }

    state.expandedControlId = controlId;
    renderControlsList();

    setTimeout(() => {
        const rowId = `grc-row-${framework}-${controlId}`;
        const rowElem = document.getElementById(rowId);
        if (rowElem) {
            rowElem.scrollIntoView({ behavior: "smooth", block: "center" });

            // Apply flash highlighting
            rowElem.style.borderColor = "var(--risk-critical)";
            rowElem.style.boxShadow = "0 0 15px rgba(239, 68, 68, 0.4)";
            
            setTimeout(() => {
                rowElem.style.borderColor = "var(--accent-cyan)";
                rowElem.style.boxShadow = "none";
            }, 1500);
        }
    }, 120);
}

// --- GLOBAL SYSTEMS INTEGRATION SYNC ---
function runIntegrationsAutomatedSync() {
    showToast("Connecting to integrations API (AWS, Okta, GitHub, Google Workspace)... Initiating compliance checks...");
    const syncBtn = elements.btnTriggerSync;
    syncBtn.innerHTML = `⏳ Collecting Evidence...`;
    syncBtn.disabled = true;

    setTimeout(() => {
        syncBtn.innerHTML = `<svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"><path d="M21.5 2v6h-6M21.34 15.57a10 10 0 1 1-.57-8.38l5.67-5.67"></path></svg> Sync Integrations`;
        syncBtn.disabled = false;

        // Auto-fix background check warning
        const hrSecurity = state.controls.find(c => c.id === "A.6");
        if (hrSecurity && hrSecurity.status === "WARNING") {
            hrSecurity.status = "PASSED";
            hrSecurity.notes += " [AUTO-SYNC: Verified Checkr onboarding logs. Background training at 100%]";
        }

        // Auto-fix access control warning
        const accessControl = state.controls.find(c => c.id === "A.9");
        if (accessControl && accessControl.status === "WARNING") {
            accessControl.status = "PASSED";
            accessControl.notes += " [AUTO-SYNC: Cleared 5 inactive admin directories via Okta identity sync]";
        }

        saveState();
        render();

        showToast("Integrations evidence successfully synced! Control objectives baseline fully operational.", "Success");
    }, 1500);
}

// --- CSV AUDIT LEDGER EXPORTER ---
function exportAuditLedger() {
    const headers = [
        "Framework", 
        "Control ID", 
        "Control Name", 
        "Control Objective",
        "Control Owner", 
        "Test Frequency", 
        "Evidence Source", 
        "Assurance Status", 
        "Inherent Risk", 
        "Residual Risk", 
        "Auditor Evidence Notes", 
        "Last Reviewed Date"
    ];

    const rows = state.controls.map(c => [
        c.framework,
        c.id,
        c.name,
        c.objective,
        c.owner,
        c.frequency,
        c.evidenceSource,
        c.status,
        c.inherentRisk,
        getResidualRisk(c.inherentRisk, c.status),
        c.notes,
        c.lastReviewed
    ]);

    const csvContent = [
        headers.join(","),
        ...rows.map(row => row.map(val => {
            const escaped = String(val).replace(/"/g, '""');
            return `"${escaped}"`;
        }).join(","))
    ].join("\n");

    const blob = new Blob([csvContent], { type: "text/csv;charset=utf-8;" });
    const url = URL.createObjectURL(blob);

    const d = new Date();
    const dateStr = `${d.getFullYear()}-${String(d.getMonth()+1).padStart(2,'0')}-${String(d.getDate()).padStart(2,'0')}`;
    const filename = `aegis_grc_compliance_export_${dateStr}.csv`;

    const link = document.createElement("a");
    link.setAttribute("href", url);
    link.setAttribute("download", filename);
    link.style.visibility = "hidden";

    document.body.appendChild(link);
    link.click();
    document.body.removeChild(link);
}

// --- BOOTSTRAP TOAST NOTIFICATION UTILITIES ---
function showToast(message, title = "Aegis GRC Engine") {
    elements.toastTitle.innerText = title;
    elements.toastMessage.innerText = message;

    const bootstrapToast = new bootstrap.Toast(elements.toastElement);
    bootstrapToast.show();
}

window.addEventListener("DOMContentLoaded", init);
