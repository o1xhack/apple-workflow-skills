import SwiftUI
struct Sample: View { var body: some View { if #available(iOS 27.1, *) { ArrangementView { Text("Primary") } secondary: { Text("Secondary") } } else { Text("Fallback") } } }
